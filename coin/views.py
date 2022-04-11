from django.http import (
    HttpResponseBadRequest,
    HttpResponseNotFound,
    HttpResponseServerError,
    JsonResponse,
)
from rest_framework.generics import CreateAPIView, RetrieveAPIView, get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication

from coin.models import Coin, PricePrediction
from coin.utils import get_current_prediction_params
from user.models import CustomUser

class ListCoins(RetrieveAPIView):
    authentication_classes = []
    permission_classes = []

    # TODO Protect
    def get(self, _):
        # TODO Cache this query.
        coins = [coin.name for coin in Coin.objects.all()]
        return JsonResponse({'coins': coins})


class RetrieveCoin(RetrieveAPIView):
    authentication_classes = []
    permission_classes = []

    # TODO Protect
    def get(self, _, name):
        # TODO Cache this query
        coin = get_object_or_404(Coin, name=name)
        params = get_current_prediction_params(coin)

        if params is None:
            return HttpResponseServerError()

        return JsonResponse(params)


class CreatePrediction(CreateAPIView):
    authentication_classes = [JWTAuthentication, ]

    def match(self, user_branches: list, real_branches: list):
        user_branches.sort()
        real_branches.sort()
        return user_branches == real_branches

    def calc_total_moz_on_branches(self, branch_values: list):
        return sum(branch_values)

    def post(self, request, name):
        coin = get_object_or_404(Coin, name=name)
        payload = request.data

        if 'branches' not in payload.keys():
            return HttpResponseBadRequest('No branch found.')

        params = get_current_prediction_params(coin)

        if params is None:
            return HttpResponseServerError()

        user_branches = list(payload['branches'].keys())
        user_values = list(payload['branches'].values())
        real_branches = params['branches']

        if not self.match(user_branches, real_branches):
            return HttpResponseBadRequest('No match between user branches and real branches.')

        # TODO Also check for floats
        if 0 < sum(1 for n in user_values if n < 0):
            return HttpResponseBadRequest('Invalid branch values.')

        total_moz = self.calc_total_moz_on_branches(user_values)
        user = CustomUser.objects.get(pk=self.request.user.id)
        remained_moz = user.num_mozcoins - total_moz

        if remained_moz < 0:
            return HttpResponseBadRequest('Not enough moz.')

        # TODO Atmoic
        user.num_mozcoins = remained_moz
        user.save()
        PricePrediction.objects.create(user=user, coin=coin, prediction=payload['branches'])

        return JsonResponse({}, status = 201)

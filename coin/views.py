from django.http import HttpResponseNotFound, JsonResponse
from rest_framework.generics import RetrieveAPIView

from pycoingecko import CoinGeckoAPI


cg = CoinGeckoAPI()
coins = {
    'btc' : {},
    'eth': {},
}
verbose_coins = {
    'btc': 'bitcoin',
    'eth': 'ethereum',
}


class ListCoins(RetrieveAPIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        return JsonResponse(coins)


class RetrieveCoin(RetrieveAPIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, name):
        if name not in coins.keys():
            return HttpResponseNotFound()

        ver_name = verbose_coins[name]
        price = cg.get_price(ids=ver_name, vs_currencies='usd')[ver_name]['usd']
        branches = ['INF',]

        # TODO
        for i in range(3, -3, -1):
            branches.append(str(int(price * (1 + i / 1000))))

        data = {
            'name': name,
            'curr_price': price,
            'm': 1, # TODO
            'n': 2, # TODO
            'branches': branches
        }

        return JsonResponse(data)


def create_prediction(req, name):
    return JsonResponse({}, status = 201)

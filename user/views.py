from django.http import JsonResponse
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

from user.models import CustomUser


class RegisterUser(CreateAPIView):
    authentication_classes = []
    permission_classes = []

    def post(self, _):
        user = CustomUser()
        user.username = str(user.uuid)
        user.save()
        refresh = RefreshToken.for_user(user)

        return JsonResponse({
            'uuid': str(user.uuid),
            'name': user.name,
            'level': user.level,
            'num_mozcoins': user.num_mozcoins,
            'token': str(refresh.access_token),
        }, status = 201)


class LoginUser(RetrieveAPIView):
    authentication_classes = [JWTAuthentication,]

    def get(self, request, *args, **kwargs):
        user = request.user
        refresh = RefreshToken.for_user(user)
        user = CustomUser.objects.get(pk=user.id)

        return JsonResponse({
            'uuid': str(user.uuid),
            'name': user.name,
            'level': user.level,
            'num_mozcoins': user.num_mozcoins,
            'token': str(refresh.access_token),
        }, status = 200)

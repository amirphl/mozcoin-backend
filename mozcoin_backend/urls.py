"""mozcoin_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from coin.views import ListCoins, RetrieveCoin, CreatePrediction
from user.views import LoginUser, RegisterUser


urlpatterns = [
    path('api/v1/users/', RegisterUser.as_view()),
    path('api/v1/users/<uuid:uuid>', LoginUser.as_view()),
    path('api/v1/coins/', ListCoins.as_view()),
    path('api/v1/coins/<str:name>', RetrieveCoin.as_view()),
    path('api/v1/coins/<str:name>/predictions/', CreatePrediction.as_view()),
    # path('admin/', admin.site.urls),
]

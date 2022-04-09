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
from django.contrib import admin
from django.urls import path
from user.views import login_user, register_user
from coin.views import get_coin_types, get_coin_info


urlpatterns = [
    path('api/v1/users/', register_user),
    path('api/v1/users/<uuid:uuid>', login_user),
    path('api/v1/coins/', get_coin_types),
    path('api/v1/coins/<str:name>', get_coin_info),
    # path('admin/', admin.site.urls),
]

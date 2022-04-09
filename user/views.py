from django.shortcuts import render
from django.http import JsonResponse


def register_user(req, *arg, **kwargs):
    return JsonResponse({
        'uuid': 'c3f2896f-2bd3-4343-90a8-26002f70f94d',
        'name': 'this-is-reg-name',
        'level': -5,
        'num_mozcoins': -49,
        'token': 'this-is-a-reg-token',
    }, status = 201)


def login_user(req, *args, **kwargs):
    return JsonResponse({
        'uuid':'c3f2896f-2bd3-4343-90a8-26002f70f94d',
        'name': 'this-is-login name',
        'level': -76,
        'num_mozcoins': 498,
        'token': 'this-is-a- *** new token ***',
    })

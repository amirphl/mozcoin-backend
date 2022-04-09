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


n = 0
def login_user(req, *args, **kwargs):
    global n
    if n == 0:
        moz = 450
        n = 1
    else:
        moz = 349
        n = 0

    return JsonResponse({
        'uuid':'c3f2896f-2bd3-4343-90a8-26002f70f94d',
        'name': 'this-is-login name',
        'level': -76,
        'num_mozcoins': moz,
        'token': 'this-is-a- *** new token ***',
    })

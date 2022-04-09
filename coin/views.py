from django.shortcuts import render
from django.http import JsonResponse


def get_coin_types(req):
    return JsonResponse({
        'btc' : {},
        'eth': {},
    })


n = 0
def get_coin_info(req, name):
    data = {'name': name}
    global n

    if n == 0:
        data['m'] = 1
        data['n'] = 1
        data['branches'] = {
            0: 3000,
            1: 2000,
            3: 4000,
            6: 45000,
        }
    if n == 1:
        data['m'] = 1
        data['n'] = 2
        data['branches'] = {
            0: 1000,
            1: 5000,
            3: -39,
            5: -39,
            7: -4444,
            -1: 4000,
        }
    if n == 2:
        data['m'] = 2
        data['n'] = 2
        data['branches'] = {
            0: 45,
            1: 69,
        }

    n += 1
    n = n % 3
    return JsonResponse(data)

def create_prediction(req, name):
    return JsonResponse({}, status = 201)

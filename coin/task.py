from __future__ import absolute_import, unicode_literals
from datetime import datetime, timedelta

from celery import shared_task
from pycoingecko import CoinGeckoAPI

from coin.models import Coin, PricePredictionParam
from coin.utils import (
    get_current_prediction_params,
    remove_sec,
    set_prediction_params,
    str_to_time,
    time_to_str,
)

M = 1
N = 2
UNIT = 'usd'
cg = CoinGeckoAPI()

def get_branches(coin):
    # TODO Handle failure.
    ver_name = coin.verbose_name
    price = cg.get_price(ids=ver_name, vs_currencies=UNIT)[ver_name][UNIT]
    branches = ['INF']

    # TODO Adjust sterategies
    for i in range(3, -3, -1):
        branches.append(str(int(price * (1 + i / 500))))

    return branches

def save_prediction_params(coin, params):
    PricePredictionParam.objects.create(
            coin=coin,
            start_at=str_to_time(params['start_at']),
            end_at=str_to_time(params['end_at']),
            eval_time=str_to_time(params['eval_time']),
            m=params['m'],
            n=params['n'],
            branches=str(params['branches'])
        )

@shared_task()
def update_prediction_params():
    curr_time = datetime.utcnow()
    coins = Coin.objects.all()

    for coin in coins:
        curr_params = get_current_prediction_params(coin)

        if curr_params is not None:
            curr_end_at = str_to_time(curr_params['end_at'])

            # TODO make it a variable # TODO true value?
            if curr_end_at - curr_time < timedelta(seconds=19):
                new_params = {
                    'start_at': time_to_str(curr_end_at),
                    'end_at': time_to_str(curr_end_at + timedelta(minutes=M)),
                    'eval_time': time_to_str(curr_end_at + timedelta(minutes=N)),
                    'm': M,
                    'n': N,
                    'branches': get_branches(coin)
                }
                set_prediction_params(coin, new_params)
                save_prediction_params(coin, new_params)
        else:
            curr_time_no_sec = remove_sec(curr_time)
            new_params = {
                "start_at": time_to_str(curr_time_no_sec),
                'end_at': time_to_str(curr_time_no_sec + timedelta(minutes=M)),
                'eval_time': time_to_str(curr_time_no_sec + timedelta(minutes = N)),
                'm': M,
                'n': N,
                'branches': get_branches(coin)
            }
            set_prediction_params(coin, new_params)
            save_prediction_params(coin, new_params)

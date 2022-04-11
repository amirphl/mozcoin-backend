from datetime import datetime
import json

from coin.contants import PREDICTION_PARAMS_REDIS_KEY_PREFIX
from coin.contants import TIME_PATTERN, TIME_PATTERN_NO_SEC
from redis_repo import redis_repo

def get_current_prediction_params(coin):
    params_bytes = redis_repo.get(PREDICTION_PARAMS_REDIS_KEY_PREFIX + coin.name)

    if params_bytes is None:
        return None

    return json.loads(params_bytes)

def set_prediction_params(coin, params):
    b = json.dumps(params)
    return redis_repo.set(PREDICTION_PARAMS_REDIS_KEY_PREFIX + coin.name, b)

def time_to_str(time: datetime) -> str:
    return datetime.strftime(time, TIME_PATTERN)

def str_to_time(time: str) -> datetime:
    return datetime.strptime(time, TIME_PATTERN)

def remove_sec(time: datetime) -> datetime:
    return datetime.strptime(datetime.strftime(time, TIME_PATTERN_NO_SEC), TIME_PATTERN_NO_SEC)

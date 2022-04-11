from django.conf import settings
import redis

class RedisRepo:
    connection = redis.Redis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            charset="utf-8",
            decode_responses=True,
            db=0,
        )

    def get(self, key):
        return self.connection.get(key)

    def hgetall(self, key):
        return self.connection.hgetall(key)

    def set(self, key, value):
        self.connection.set(key, value)

    def hmset(self, key, value):
        self.connection.hmset(key, value)

redis_repo = RedisRepo()

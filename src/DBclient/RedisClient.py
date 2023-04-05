import redis
from src.config import REDIS_HOST, REDIS_PORT


class RedisClient:
    def __init__(self):
        self.__r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

    def add_set_element(self, key: str, value: str):
        try:
            self.__r.sadd(key, value)
        except Exception as e:
            print("Add to key {} fail value is {}\nError is: {}".format(key, value, e))

    def delete_set_element(self, key: str, value: str):
        try:
            self.__r.srem(key, value)
        except Exception as e:
            print("Delete from key {} fail value is {}\nError is: {}".format(key, value, e))

    def get_set_elements(self, key: str):
        try:
            elements = self.__r.smembers(key)
            return elements
        except Exception as e:
            print("Get {} elements fail\nError is: {}".format(key, e))

    def get_set_elements_count(self, key: str):
        try:
            count = self.__r.scard(key)
            return count
        except Exception as e:
            print("Get {} count fail\nError is: {}".format(key, e))

    def set_random_pop(self, key: str):
        try:
            element = self.__r.spop(key)
            return element
        except Exception as e:
            print("Random pop element from {} fail\nError is: {}".format(key, e))
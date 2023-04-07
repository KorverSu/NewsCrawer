import time
import random

from src.crawer.url_collector import URLCollector
from src.DBclient.redis_client import RedisClient
from src.config import DRIVER_PATH, PTS_NUM, TVBS_NUM, SETN_NUM
if __name__ == '__main__':
    collector = URLCollector()
    collector.collect_new_pts_url()

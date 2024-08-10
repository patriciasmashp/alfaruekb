import datetime
from dotenv import load_dotenv
from os import environ, path
from loguru import logger

load_dotenv()

TOKEN = environ["TOKEN"]
DB_URL = environ["DB_URL"]
DB_ASYNC_DRIVER = environ["DB_ASYNC_DRIVER"]
DB_SYNC_DRIVER = environ["DB_SYNC_DRIVER"]
DEBUG = int(environ["DEBUG"])
PAGES_SIZE = 5
BASE_PATH = path.dirname(path.realpath(__file__))

# RABBIT_MQ_URL = environ["RABBIT_MQ_URL"]
# REDIS_HOST = environ["REDIS_HOST"]
# REDIS_PORT = environ["REDIS_PORT"]


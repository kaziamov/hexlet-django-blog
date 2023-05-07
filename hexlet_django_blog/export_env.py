import dotenv
import os
from urllib.parse import urlparse

dotenv.load_dotenv()
env_get = os.environ.get


ALLOWED_HOST = env_get('ALLOWED_HOST')

DATABASE_URL = urlparse(env_get('DATABASE_URL'))

if DATABASE_URL:
    DB_HOST = DATABASE_URL.hostname
    DB_PORT = DATABASE_URL.port
    DB_NAME = DATABASE_URL.path[1:]
    DB_USER = DATABASE_URL.username
    DB_PASS = DATABASE_URL.password
else:
    DB_HOST = env_get('DB_HOST')
    DB_PORT = env_get('DB_PORT')
    DB_NAME = env_get('DB_NAME')
    DB_USER = env_get('DB_USER')
    DB_PASS = env_get('DB_PASS')


import environ
from dotenv import load_dotenv

load_dotenv()

env = environ.Env()


environ.Env.read_env()

CLOUDRUN_SERVICE_URL = env('CLOUDRUN_SERVICE_URL', default=None)
BUCKET_URL = env('BUCKET_URL', default=None)
APP_NAME = env('APP_NAME', default=None)
PORT = env('PORT', default=None)
APP_ENV = env('APP_ENV', default=None)
SECREY_KEY = env('SECRET_KEY', default=None)



DEBUG = APP_ENV == 'local' or APP_ENV == 'dev'
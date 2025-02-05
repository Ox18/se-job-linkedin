
import environ
from dotenv import load_dotenv

load_dotenv()
env = environ.Env()
environ.Env.read_env()

JWT_SECRET_KEY = env('JWT_SECRET_KEY', default=None)
import jwt
import datetime
from shared.config import JWT_SECRET_KEY

def encrypt(data):
    payload = data
    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(hours=1)

    return jwt.encode(payload, JWT_SECRET_KEY, algorithm='HS256')

def decrypt(token):
    return jwt.decode(token, JWT_SECRET_KEY, algorithms=['HS256'])
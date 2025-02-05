from django.utils.deprecation import MiddlewareMixin
from shared.utils.http import HttpRequest
from shared.utils.jwt import decrypt
from errors.common import UnauthorizedException
import requests
from requests.cookies import RequestsCookieJar

class SecureSessionMiddleware(MiddlewareMixin):
    def process_request(self, request: HttpRequest):
        if request.path.startswith('/secure/'):
            authorization = request.headers.get('Authorization')
            if not authorization:
                return self.unauthorizaed_response('Authorization header is required')
            
            try:
                decrypted_data = decrypt(authorization)
                request.__setattr__('auth', decrypted_data)
                call = requests.session()
                call.headers['Csrf-Token'] = decrypted_data['csrf']
                call.headers['Accept'] = 'application/json'
                call.headers['Content-Type'] = 'application/json'
                cookie_jar = RequestsCookieJar()
                for key, value in decrypted_data['cookies'].items():
                    cookie_jar.set(key, value)
                call.cookies = cookie_jar

                request.__setattr__('call', call)
            except Exception as e:
                return self.unauthorizaed_response('Invalid token')
            
    def unauthorizaed_response(self, message: str):
            return UnauthorizedException(message).toResponse()
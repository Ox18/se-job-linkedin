from django.utils.deprecation import MiddlewareMixin
from shared.utils.http import HttpRequest
from shared.utils.jwt import decrypt
from errors.common import UnauthorizedException

class SecureSessionMiddleware(MiddlewareMixin):
    def process_request(self, request: HttpRequest):
        if request.path.startswith('/secure/'):
            authorization = request.headers.get('Authorization')
            if not authorization:
                return self.unauthorizaed_response('Authorization header is required')
            
            try:
                request.__setattr__('auth', decrypt(authorization))
            except Exception as e:
                print(e)
                return self.unauthorizaed_response('Invalid token')
            
    def unauthorizaed_response(self, message: str):
            return UnauthorizedException(message).toResponse()
from django.http import JsonResponse, HttpRequest
from django.utils.decorators import method_decorator


class Response:
    @staticmethod
    def ok(data, message):
        return JsonResponse({
            'success': True,
            'message': message,
            'data': data
        })
    
    @staticmethod
    def error(message):
        return JsonResponse({
            'success': False,
            'message': message,
            'data': {
                'error': message
            }
        })
    

class AuthParams:
    cookies: dict = {}
    csrf: str = ''

class SecureHttpRequest(HttpRequest):
    auth: AuthParams = AuthParams()

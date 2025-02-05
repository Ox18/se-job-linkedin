from django.http import JsonResponse

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
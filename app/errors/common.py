from .base import BaseException

class BadRequestException(BaseException):
    def __init__(self, message):
        super().__init__(message, {}, {
            'name': 'BadRequestException',
            'status': 400,
        })

class UnauthorizedException(BaseException):
    def __init__(self, message):
        super().__init__(message, {}, {
            'name': 'UnauthorizedException',
            'status': 401,
       })
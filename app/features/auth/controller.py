from main.utils.response import Response
from django.http import HttpRequest
from .services.auth_service import AuthService
import json

class AuthController():
    def __init__(self, authService: AuthService):
        self.authService = authService

    def login(self, request: HttpRequest):
        data = json.loads(request.body)
        response = self.authService.login(data['username'], data['password'])
        return Response.ok(response, 'Login success')

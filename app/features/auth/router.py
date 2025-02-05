from django.urls import path

from .controller import AuthController
from .services.auth_service import AuthService
from .repositories.session_repository import SessionRepository
from shared.gateways.linkedin_auth import LinkedinAuthGateway

linkedinAuthGateway = LinkedinAuthGateway()

sessionRepository = SessionRepository()

authService = AuthService(sessionRepository, linkedinAuthGateway)

authController = AuthController(authService)

urlpatterns = [
    path('auth/login', authController.login, name='auth_login')
]
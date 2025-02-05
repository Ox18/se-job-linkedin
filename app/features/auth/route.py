from django.urls import path

from .controller import AuthController
from .services.auth_service import AuthService
from .repositories.session_repository import SessionRepository
from shared.gateways.linkedin import LinkedinGateway

linkedinGateway = LinkedinGateway()

sessionRepository = SessionRepository()

authService = AuthService(sessionRepository, linkedinGateway)

authController = AuthController(authService)

urlpatterns = [
    path('auth/login', authController.login, name='auth_login')
]
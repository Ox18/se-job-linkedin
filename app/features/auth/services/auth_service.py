from ..repositories.session_repository import SessionRepository
from shared.gateways.linkedin import LinkedinGateway

class AuthService:
    def __init__(self, session_repository: SessionRepository, linkedin_gateway: LinkedinGateway):
        self.session_repository = session_repository
        self.linkedin_gateway = linkedin_gateway

    def login(self, username: str, password: str):
        response = self.linkedin_gateway.authenticate(username, password)

        token = self.session_repository.create(response)

        return {
            'token': token,
            'response': response
        }
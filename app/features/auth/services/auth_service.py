from ..repositories.session_repository import SessionRepository
from shared.gateways.linkedin_auth import LinkedinAuthGateway
import uuid

class AuthService:
    def __init__(self, session_repository: SessionRepository, linkedin_auth_gateway: LinkedinAuthGateway):
        self.session_repository = session_repository
        self.linkedin_auth_gateway = linkedin_auth_gateway

    def login(self, username: str, password: str):
        response = self.linkedin_auth_gateway.authenticate(username, password)
        identifier = str(uuid.uuid4())
        response['identifier'] = identifier
        token = self.session_repository.create(response)

        return {
            'token': token
        }
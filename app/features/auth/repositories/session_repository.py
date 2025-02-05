import shared.utils.jwt as jwt
from shared.gateways.linkedin import LinkedinGateway

class SessionRepository:
    def get(self, token: str):
        return jwt.decrypt(token)


    def create(self, data: dict):
        token = jwt.encrypt(data)
        return token
import shared.utils.jwt as jwt

class SessionRepository:
    def get(self, token: str):
        return jwt.decrypt(token)
    
    def create(self, data: dict):
        token = jwt.encrypt(data)
        return token
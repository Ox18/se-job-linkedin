from .service import HealthcheckService
from shared.utils.http import HttpRequest, Response

class HealthcheckController:
    def __init__(self, healthcheckService: HealthcheckService):
        self.healtcheckService = healthcheckService

    def check(self, request: HttpRequest):
        response = self.healtcheckService.check()
    
        return Response.ok(response, 'Healthcheck is OK')
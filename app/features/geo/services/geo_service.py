import requests
from shared.gateways.linkedin_api import LinkedinApiGateway

class GeoService:
    def __init__(self, linkedin_api: LinkedinApiGateway):
        self.linkedin_api = linkedin_api

    def search(self, keywords: str, call: requests):
        items = self.linkedin_api.geo(keywords, call)

        return items
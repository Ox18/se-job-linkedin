import requests
from shared.gateways.linkedin_api import LinkedinApiGateway

class JobService:
    def __init__(self, linkedin_api: LinkedinApiGateway):
        self.linkedin_api = linkedin_api

    def getFormJob(self, jobPostingId: int, call: requests):
        return self.linkedin_api.getFormJob(jobPostingId, call)
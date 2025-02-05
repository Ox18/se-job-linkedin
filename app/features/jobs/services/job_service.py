import requests
from shared.gateways.linkedin_api import LinkedinApiGateway

class JobService:
    def __init__(self, linkedin_api: LinkedinApiGateway):
        self.linkedin_api = linkedin_api

    def getFormJob(self, job_id: int, call: requests):
        return self.linkedin_api.getForm(job_id, call)
        
import requests
from shared.gateways.linkedin_api import LinkedinApiGateway
from features.jobs.adapters.question_adapter import formAdapter

class JobService:
    def __init__(self, linkedin_api: LinkedinApiGateway):
        self.linkedin_api = linkedin_api

    def getFormJob(self, jobPostingId: int, call: requests):
        formJob = self.linkedin_api.getFormJob(jobPostingId, call)

        return formAdapter(formJob)

    def suggestJob(self, keywords: str, call: requests):
        jobs = self.linkedin_api.suggestJob(keywords, call)

        return jobs

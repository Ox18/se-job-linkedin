from shared.utils.http import Response, method_decorator, SecureHttpRequest
from shared.decorators.handle_request import handle_request
from .services.job_service import JobService

class JobsController:
    def __init__(self, job_service: JobService):
        self.job_service = job_service
    
    @method_decorator(handle_request)
    def getFormJob(self, request: SecureHttpRequest):
        jobPostingId = request.GET.get('jobPostingId')

        jobForm = self.job_service.getFormJob(jobPostingId, request.call)

        return Response.ok(jobForm, "Get job form")
    
    @method_decorator(handle_request)
    def suggestJob(self, request: SecureHttpRequest):
        keywords = request.GET.get('keywords')

        jobs = self.job_service.suggestJob(keywords, request.call)

        return Response.ok(jobs, "Suggest job")
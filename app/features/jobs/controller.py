from shared.utils.http import Response, method_decorator, SecureHttpRequest
from shared.decorators.handle_request import handle_request
from shared.gateways.linkedin_api import LinkedinApiGateway
from .services.job_service import JobService

linkedinApiGateway = LinkedinApiGateway()
class JobsController:
    def __init__(self, job_service: JobService):
        self.job_service = job_service
    
    @method_decorator(handle_request)
    def getFormJob(self, request: SecureHttpRequest):
        jobPostingId = request.GET.get('jobPostingId')

        jobForm = self.job_service.getFormJob(jobPostingId, request.call)

        return Response.ok(jobForm, "Get job form")
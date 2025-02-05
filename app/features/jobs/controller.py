from shared.utils.http import Response, method_decorator, SecureHttpRequest
from shared.decorators.handle_request import handle_request
from shared.gateways.linkedin_api import LinkedinApiGateway

linkedinApiGateway = LinkedinApiGateway()
class JobsController:
    @method_decorator(handle_request)
    def search(self, request: SecureHttpRequest):
        print('request', request)
        call = request.call
        print('call', call)
        print(call.cookies)
        jobForm = linkedinApiGateway.getForm(1, call)
        print('jobForm', jobForm)

        return Response.ok({
            "jobForm": jobForm
        }, "Search jobs")
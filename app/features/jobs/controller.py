from shared.utils.http import Response, method_decorator, SecureHttpRequest
from shared.decorators.handle_request import handle_request

class JobsController:
    @method_decorator(handle_request)
    def search(self, request: SecureHttpRequest):
        return Response.ok({
            'message': 'Search jobs',
            'session': request.auth['cookies']
        }, "Search jobs")
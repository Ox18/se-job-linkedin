from shared.utils.http import Response, HttpRequest, method_decorator
from .service import HomeService
from shared.decorators.handle_request import handle_request

import logging

logger = logging.getLogger(__name__)

class HomeController:
    def __init__(self, homeService: HomeService):
        self.homeService = homeService

    @method_decorator(handle_request)
    def index(self, request: HttpRequest):
        trace_id = request.headers.__dict__.get('X-Trace-ID')
        logger.info(f'Trace ID: {trace_id} - Home Controller')
    
        response = self.homeService.main()

        return Response.ok(response, 'Home is OK')
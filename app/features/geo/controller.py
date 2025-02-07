from shared.utils.http import Response, method_decorator, SecureHttpRequest
from shared.decorators.handle_request import handle_request
from .services.geo_service import GeoService

class GeoController:
    def __init__(self, geo_service: GeoService):
        self.geo_service = geo_service

    @method_decorator(handle_request)
    def getGeo(self, request: SecureHttpRequest):
        keywords = request.GET.get('keywords', '')
        geo = self.geo_service.search(keywords, request.call)

        return Response.ok(geo, "Get geo")
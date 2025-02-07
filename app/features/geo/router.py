from django.urls import path
from shared.gateways.linkedin_api import LinkedinApiGateway
from .controller import GeoController
from .services.geo_service import GeoService


linkedinApiGateway = LinkedinApiGateway()

service = GeoService(linkedinApiGateway)
controller = GeoController(service)

urlpatterns = [
    path('secure/geo', controller.getGeo, name='geo_getGeo')
]
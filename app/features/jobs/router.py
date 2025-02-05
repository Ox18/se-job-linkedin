from django.urls import path
from shared.gateways.linkedin_api import LinkedinApiGateway
from .controller import JobsController


linkedinApiGateway = LinkedinApiGateway()
jobsController = JobsController(linkedinApiGateway)

urlpatterns = [
    path('secure/jobs/search', jobsController.search, name='jobs_search')
]
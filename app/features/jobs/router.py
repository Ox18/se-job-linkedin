from django.urls import path
from shared.gateways.linkedin_api import LinkedinApiGateway
from .controller import JobsController
from .services.job_service import JobService


linkedinApiGateway = LinkedinApiGateway()

jobService = JobService(linkedinApiGateway)

jobsController = JobsController(jobService)

urlpatterns = [
    path('secure/jobs/form', jobsController.getFormJob, name='jobs_getFormJob'),
    path('secure/jobs/suggest', jobsController.suggestJob, name='jobs_suggestJob')
]
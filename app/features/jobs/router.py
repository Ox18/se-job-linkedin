from django.urls import path

from .controller import JobsController


jobsController = JobsController()

urlpatterns = [
    path('secure/jobs/search', jobsController.search, name='jobs_search')
]
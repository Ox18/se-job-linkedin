from django.urls import path
from .controller import HomeController
from .service import HomeService

homeService = HomeService()

homeController = HomeController(homeService)

urlpatterns = [
    path('', homeController.index, name='home')
]
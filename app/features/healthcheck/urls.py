from django.urls import path
from .controller import HealthcheckController
from .service import HealthcheckService


healtcheckService = HealthcheckService()
healthcheck_controller = HealthcheckController(healtcheckService)

urlpatterns = [
    path('healthcheck/', healthcheck_controller.check, name='healthcheck'),
]
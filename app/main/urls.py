from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('features.home.urls')),
    path('', include('features.healthcheck.urls')),
    path('', include('features.auth.router')),
    path('', include('features.jobs.router')),
    path('', include('features.geo.router')),
    path('admin/', admin.site.urls),
]

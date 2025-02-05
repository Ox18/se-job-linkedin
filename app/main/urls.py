from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('', include('healthcheck.urls')),
    path('', include('features.auth.route')),
    path('admin/', admin.site.urls),
]

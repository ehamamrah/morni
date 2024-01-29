from django.contrib import admin
from django.urls import path, include
from services import urls as services_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('services/', include(services_urls)),
]

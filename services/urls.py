from django.urls import path, include
from services.v1.views import (
    ServiceListApiView,
    ServiceRequestApiView
)

urlpatterns = [
    path('', ServiceListApiView.as_view()),
    path('request', ServiceRequestApiView.as_view()),
]

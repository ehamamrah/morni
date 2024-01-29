from django.urls import path, include
from services.v1.views import (
    ServiceListApiView,
)

urlpatterns = [
    path('', ServiceListApiView.as_view()),
]

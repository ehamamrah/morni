from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from services.models import Service
from .serializers import ServicesSerializer
import logging
logger = logging.getLogger(__name__)

class ServiceListApiView(APIView):
    def get(self, request, *args, **kwargs):
        longitude = request.query_params.get("longitude", None)
        latitude = request.query_params.get("latitude", None)
        logger.info(request)
        logger.info("longitude: %s, latitude: %s", longitude, latitude)
        services = Service.active_services_in_area(longitude, latitude)
        serializer = ServicesSerializer(services, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

from rest_framework.views import APIView
from rest_framework import generics

from rest_framework.response import Response
from rest_framework import status
from services.models import Service
from .serializers import ServicesSerializer, ServiceRequestSerializer
from services.managers import ServiceRequestDataHandler

class ServiceListApiView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        # This is customer location details
        longitude = request.query_params.get("longitude", None)
        latitude = request.query_params.get("latitude", None)

        if longitude is None or latitude is None:
            services = Service.active_services()
        else:
            services = Service.active_services_in_area(longitude, latitude)

        serializer = ServicesSerializer(services, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ServiceRequestApiView(generics.CreateAPIView):
    def get_authenticate_header(self, request):
        return super().get_authenticate_header(request)

    def post(self, request, *args, **kwargs):
        service_id = request.data.get("service_id", None)

        # Customer Details
        mobile_number = request.data.get("mobile_number", None)
        longitude = request.data.get("longitude", None)
        latitude = request.data.get("latitude", None)

        service_request_data = ServiceRequestDataHandler(service_id, latitude, longitude, mobile_number).get_data()
        serializer = ServiceRequestSerializer(data=service_request_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

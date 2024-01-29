from services.models import Service, ServiceRequest
from rest_framework import serializers


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ("id", "name", "enabled", "area")
        extra_kwargs = {"area": {"read_only": True}}


class ServiceRequestSerializer(serializers.Serializer):
    service_id = serializers.IntegerField()
    provider_id = serializers.IntegerField()
    mobile_number = serializers.CharField(max_length=15)
    longitude = serializers.FloatField()
    latitude = serializers.FloatField()

    class Meta:
        model = ServiceRequest
        extra_kwargs = {"service_id": {"read_only": True}, "provider_id": {"read_only": True}}

    def create(self, validated_data):
        return ServiceRequest.objects.create(**validated_data)

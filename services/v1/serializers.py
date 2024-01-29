from services.models import Service
from rest_framework import serializers


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ("id", "name", "enabled", "area")
        extra_kwargs = {"area": {"read_only": True}}

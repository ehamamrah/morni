from providers.models import Provider
from rest_framework import serializers


class ProvidersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ("id", "name", "enabled", "location")
        extra_kwargs = {"location": {"read_only": True}}

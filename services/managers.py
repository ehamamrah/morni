from services.models import Service
from providers.models import Provider
from django.contrib.gis.measure import Distance
from django.contrib.gis.geos import Point
from morni.settings import GEO_ALLOWED_KM

class ServiceRequestDataHandler:
    def __init__(self, service_id, latitude, longitude, mobile_number):
        self.longitude = float(longitude)
        self.latitude = float(latitude)
        self.service = Service.objects.get(id = service_id)
        self.mobile_number = mobile_number

    def get_provider(self):
        list_of_providers_ids = self.service.providerservice_set.values_list("provider_id", flat = True)
        if list_of_providers_ids.exists() == False:
            return None
        list_of_providers = Provider.objects.filter(id__in = list_of_providers_ids)
        if list_of_providers.exists() == False:
            return None
        point = Point(self.longitude, self.latitude, srid = 4326)
        nearest_provider = list_of_providers.filter(location__distance_lt=(point, Distance(km=GEO_ALLOWED_KM))).order_by("location")

        if nearest_provider.exists() == False:
            return None
        else:
            return nearest_provider.first().id

    def get_data(self):
        return {
            "service_id": self.service.id,
            "provider_id": self.get_provider(),
            "mobile_number": self.mobile_number,
            "longitude": self.longitude,
            "latitude": self.latitude
        }

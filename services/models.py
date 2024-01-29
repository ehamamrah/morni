from django.contrib.gis.db import models
from django.contrib.gis.measure import Distance
from django.contrib.gis.geos import Point
from morni.settings import GEO_ALLOWED_KM

class Service(models.Model):
    name = models.CharField(max_length = 180, blank = False, null = False)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    enabled = models.BooleanField(default = True)
    area = models.MultiPolygonField(blank = False, null = False)

    def __str__(self):
        return self.name

    @classmethod
    def active_services(cls):
        return cls.objects.filter(enabled = True).all()

    @classmethod
    def active_services_in_area(cls, longitude, latitude):
        longitude = float(longitude)
        latitude = float(latitude)
        point = Point(longitude, latitude, srid = 4326)
        return cls.active_services().filter(area__distance_lt=(point, Distance(km=GEO_ALLOWED_KM)))

    def active_providers(self):
        return self.provider_set.filter(enabled = True).all()

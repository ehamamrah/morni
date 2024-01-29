from django.contrib.gis.db import models
from services.models import Service

class Provider(models.Model):
    name = models.CharField(max_length = 180, blank = False, null = False)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    enabled = models.BooleanField(default = True)
    location = models.PointField(blank = False, null = False)

    def __str__(self):
        return self.name

class ProviderService(models.Model):
    provider = models.ForeignKey(Provider, on_delete = models.CASCADE)
    service = models.ForeignKey(Service, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

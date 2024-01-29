from django.contrib.gis.db import models

class Service(models.Model):
    name = models.CharField(max_length = 180, blank = False, null = False)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    enabled = models.BooleanField(default = True)
    area = models.MultiPolygonField(blank = False, null = False)

    def __str__(self):
        return self.name

    def active_providers(self):
        return self.provider_set.filter(enabled = True).all()

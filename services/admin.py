from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin
from .models import Service

@admin.register(Service)
class ServiceAdmin(GISModelAdmin):
    list_display = ('name', 'enabled')

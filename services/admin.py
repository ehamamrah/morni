from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin
from .models import Service, ServiceRequest

@admin.register(Service)
class ServiceAdmin(GISModelAdmin):
    list_display = ('name', 'enabled')

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('service', 'provider', 'mobile_number', 'timestamp')

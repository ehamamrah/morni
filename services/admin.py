from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin
from .models import Service, ServiceRequest

@admin.register(Service)
class ServiceAdmin(GISModelAdmin):
    list_display = ('name', 'enabled')

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    def get_status(self, obj):
        return obj.get_status_display()
    get_status.short_description = 'Status'

    list_display = ('service', 'provider', 'mobile_number', 'get_status', 'timestamp')

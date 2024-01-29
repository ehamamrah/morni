from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin
from .models import Provider, ProviderService

@admin.register(Provider)
class ProviderAdmin(GISModelAdmin):
    list_display = ('name', 'location')

@admin.register(ProviderService)
class ProviderServiceAdmin(admin.ModelAdmin):
    list_display = ('provider', 'service')

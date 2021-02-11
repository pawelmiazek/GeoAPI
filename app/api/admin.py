from django.contrib import admin
from .models import GeoLocation

# Register your models here.


@admin.register(GeoLocation)
class GeoLocationAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'url', 'latitude', 'longitude')
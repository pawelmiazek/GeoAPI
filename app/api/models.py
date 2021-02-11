from django.db import models

class GeoLocation(models.Model):
    class Meta:
        verbose_name = "GeoLocation"
        verbose_name_plural = "GeoLocations"

    ip_address = models.CharField("IP adress", max_length=100, unique=True)
    url = models.CharField("URL", max_length=100, null=True, blank=True)
    continent = models.CharField("Continent", max_length=150, blank=True)
    country = models.CharField("Country", max_length=150, blank=True)
    city = models.CharField("City", max_length=150, blank=True)
    latitude = models.FloatField("Latitude", blank=True)
    longitude = models.FloatField("Longitude", blank=True)

    def __str__(self):
        return f"{self.ip_address}({self.url or ''})"
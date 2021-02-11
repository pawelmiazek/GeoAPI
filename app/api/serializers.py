from rest_framework import serializers
from .models import GeoLocation
import requests
import re
from django.contrib.auth.models import User


class GeoLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoLocation
        fields = '__all__'
        read_only_fields = ('url', 'continent', 'country', 'city',
                            'latitude', 'longitude')
    
    def save(self):
        ip_address = self.validated_data.get('ip_address')
        ip_with_letters = re.search('[a-zA-Z]', ip_address)
        access_key = '18caaf446159eaf16ddbbe011a060c85'
        r = requests.get(
            f'http://api.ipstack.com/{ip_address}?access_key={access_key}'
        )
        data = r.json()
        existing_ip_addresses = [location.ip_address for location in GeoLocation.objects.all()]
        if data['ip'] in existing_ip_addresses:
            raise serializers.ValidationError(
                "The specified address IP already exists in database."
            )
        if not data['latitude'] or not data['latitude']:
            raise serializers.ValidationError(
                "The specified address IP or URL does not exist."
            )
        else:
            create_data = {
                'ip_address': data['ip'],
                'continent': data['continent_name'],
                'country': data['country_name'],
                'city': data['city'],
                'latitude': data['latitude'],
                'longitude': data['longitude'],
                'url': ip_address if ip_with_letters else '',
            }
            if self.instance:
                self.instance.ip_address = data['ip']
                self.instance.continent = data['continent_name']
                self.instance.country = data['country_name']
                self.instance.city = data['city']
                self.instance.latitude = data['latitude']
                self.instance.longitude = data['longitude']
                self.instance.url = ip_address if ip_with_letters else ''
                return self.instance.save()
            else:
                return GeoLocation.objects.create(**create_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

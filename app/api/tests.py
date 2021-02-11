from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from .models import GeoLocation
from django.contrib.auth.models import User


class GetAllGeoLocationsTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='john', password='john123!')
        self.refresh = RefreshToken.for_user(self.user)
        self.geo_1 = GeoLocation.objects.create(ip_address="89.64.1.177")
        self.geo_2 = GeoLocation.objects.create(ip_address="95.216.162.175")

        self.valid_data = {
            'ip_address': "217.74.65.23"
        }
        self.invalid_data_1 = {
            'ip_address': "89.64.1.177"
        }
        self.invalid_data_2 = {
            'ip_address': "funnyip"
        }
        self.new_user = {
            'username': 'mark',
            'password': 'mark123!'
        }
    
    def test_geolocation_list(self):
        url = reverse('api:geolocation-list-create')
        self.client.credentials(
            HTTP_AUTHORIZATION=f"JWT {self.refresh.access_token}"
        )
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_geolocation_delete(self):
        url = reverse(
            'api:geolocation-update-delete', kwargs={'pk': self.geo_1.pk}
        )
        self.client.credentials(
            HTTP_AUTHORIZATION=f"JWT {self.refresh.access_token}"
        )
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_geolocation_detail(self):
        url = reverse(
            'api:geolocation-update-delete', kwargs={'pk': self.geo_1.pk}
        )
        self.client.credentials(
            HTTP_AUTHORIZATION=f"JWT {self.refresh.access_token}"
        )
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_geolocation_update(self):
        url = reverse(
            'api:geolocation-update-delete', kwargs={'pk': self.geo_1.pk}
        )
        self.client.credentials(
            HTTP_AUTHORIZATION=f"JWT {self.refresh.access_token}"
        )
        response = self.client.put(url, self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_geolocation_update_not_unique(self):
        url = reverse(
            'api:geolocation-update-delete', kwargs={'pk': self.geo_1.pk}
        )
        self.client.credentials(
            HTTP_AUTHORIZATION=f"JWT {self.refresh.access_token}"
        )
        response = self.client.put(url, self.invalid_data_1, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_geolocation_create(self):
        url = reverse('api:geolocation-list-create')
        self.client.credentials(
            HTTP_AUTHORIZATION=f"JWT {self.refresh.access_token}"
        )
        response = self.client.post(url, self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_geolocation_create_validation(self):
        url = reverse('api:geolocation-list-create')
        self.client.credentials(
            HTTP_AUTHORIZATION=f"JWT {self.refresh.access_token}"
        )
        response = self.client.post(url, self.invalid_data_2, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_user_register(self):
        url = reverse('api:user-create')
        response = self.client.post(url, self.new_user, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_authorized(self):
        url = reverse('api:geolocation-list-create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

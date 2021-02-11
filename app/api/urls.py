from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.api_overview, name='api-overview'),
    path('geolocations/', views.GeoLocationListCreate.as_view(), name='geolocation-list-create'),
    path('geolocations/<int:pk>/', views.GeoLocationUpdateDelete.as_view(), name='geolocation-update-delete')
]
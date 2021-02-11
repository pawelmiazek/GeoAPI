from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'api'

urlpatterns = [
    path('', views.api_overview, name='api-overview'),
    path('geolocations/', views.GeoLocationListCreate.as_view(), name='geolocation-list-create'),
    path('geolocations/<int:pk>/', views.GeoLocationUpdateDelete.as_view(), name='geolocation-update-delete'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.UserCreate.as_view(), name='user-create'),
]

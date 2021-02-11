from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import AllowAny

from .serializers import GeoLocationSerializer, UserSerializer
from .models import GeoLocation
from django.contrib.auth.models import User


@api_view(['GET'])
@permission_classes([AllowAny, ])
def api_overview(request, format=None):
    api_urls = {
        'GeoLocation List & Create': reverse('api:geolocation-list-create', request=request, format=format),
        'User Create': reverse('api:user-create', request=request, format=format),
    }
    return Response(api_urls)


class GeoLocationListCreate(generics.ListCreateAPIView):
    queryset = GeoLocation.objects.all()
    serializer_class = GeoLocationSerializer


class GeoLocationUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = GeoLocation.objects.all()
    serializer_class = GeoLocationSerializer


class UserCreate(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer

from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .serializers import GeoLocationSerializer
from .models import GeoLocation


@api_view(['GET'])
def api_overview(request, format=None):
    api_urls = {
        'GeoLocation List': reverse('api:geolocation-list-create', request=request, format=format),
    }
    return Response(api_urls)


class GeoLocationListCreate(generics.ListCreateAPIView):
    queryset = GeoLocation.objects.all()
    serializer_class = GeoLocationSerializer


class GeoLocationUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = GeoLocation.objects.all()
    serializer_class = GeoLocationSerializer

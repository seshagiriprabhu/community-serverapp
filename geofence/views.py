from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt

from rest_framework import generics, filters, status, viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from geofence.serializers import GeofenceSerializer
from geofence.serializers import GeofenceListSerializer
from geofence.serializers import GeofenceDetailsSerializer
from geofence.serializers import GeofenceGIDSerializer


class GeofenceViewSet(generics.ListCreateAPIView):
    """
    (Graphical) API endpoint that allows user geofence data  
    to be added or viewed
    """
    serializer_class = GeofenceSerializer
    def get(self, request, *args, **kwargs):
        queryset = Geofence.objects.all().reverse()[:5]
        serializer = GeofenceGIDSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = GeofenceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,\
                    status=status.HTTP_201_CREATED)
        return Response(serializer.errors,\
                status=status.HTTP_400_BAD_REQUEST)


class GeofenceListViewSet(APIView):
    serializer_class = GeofenceListSerializer
    def get(self, request, *args, **kwargs):
        queryset = Geofence.objects.all().reverse()
        serializer = GeofenceListSerializer(queryset, many=True)
        return Response(serializer.data)


class GeofenceNameSearchDetailsViewset(APIView):
    serializer_class = GeofenceSerializer
    def get_object(self, fence_name):
        try:
            return Geofence.objects.all().filter(fence_name=fence_name)
        except Geofence.DoesNotExist:
            raise Http404

    def get(self, request, fence_name, format=None):
        queryset = self.get_object(fence_name)
        serializer = GeofenceDetailsSerializer(queryset, many=True)
        return Response(serializer.data)


class GeofenceDetailsViewSet(APIView):
    serializer_class = GeofenceDetailsSerializer
    def get_object(self, gid):
        try:
            return Geofence.objects.get(gid=gid)
        except Geofence.DoesNotExist:
            raise Http404

    def get(self, request, gid, format=None):
        queryset = self.get_object(gid)
        serializer = GeofenceDetailsSerializer(queryset)
        return Response(serializer.data)

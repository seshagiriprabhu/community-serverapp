from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt

from rest_framework import generics, filters, status, viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from userlocation.models import Geofence, UserLocationData
from userlocation.models import UserPhoneData
from userlocation.serializers import GeofenceSerializer
from userlocation.serializers import UserLocationSerializer
from userlocation.serializers import UserPhoneDataSerializer


class UserLocationViewSet(generics.ListCreateAPIView):
    """
    (Graphical) API endpoint that allows user location data 
    to be added or viewed
    """
    serializer_class = UserLocationSerializer
    def get(self, request, *args, **kwargs):
        queryset = UserLocationData.objects.all()
        serializer = UserLocationSerializer(queryset, many=True)
        return Response(serializer.data) 

    def post(self, request, *args, **kwargs):
        serializer = UserLocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GeofenceViewSet(generics.ListCreateAPIView):
    """
    (Graphical) API endpoint that allows user geofence data  
    to be added or viewed
    """
    serializer_class = GeofenceSerializer
    def get(self, request, *args, **kwargs):
        queryset = Geofence.objects.all()
        serializer = GeofenceSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = GeofenceSerializer(data=request.data)
        if serializer.is_valid():
            expiration_time = request.data['expiration_time']
            if int(expiration_time) > 0:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else: 
                return Response('Error: Expiration time should be valid value')
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'POST'])
def userlocation(request):
    if request.method == 'GET':
        location_list = UserLocationData.objects.all()
        serializer = UserLocationSerializer(location_list, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        serializer = UserLocationSerializer(data=request.data)
        if serializer.is_valid():
            if serializer.objects.transition_type > -2 and \
                    serializer.objects.transition_type < 5 and \
                    serializer.objects.accuracy < 100.0 and \
                    serializer.objects.accuracy > 0.0:
                serializer.save()
                return JSONResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JSONResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


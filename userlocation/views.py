from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt

from rest_framework import generics, filters, status, viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from userlocation.models import Geofence, UserLocationData
from userlocation.serializers import GeofenceSerializer
from userlocation.serializers import GeofenceListSerializer
from userlocation.serializers import GeofenceDetailsSerializer
from userlocation.serializers import GeofenceGIDSerializer
from userlocation.serializers import UserLocationSerializer
from userlocation.serializers import UserLocationListSerializer
from userlocation.serializers import UserLocationDetailsSerializer

from registeration.views import JSONResponse

class UserLocationViewSet(generics.ListCreateAPIView):
    """
    (Graphical) API endpoint that allows user location data 
    to be added or viewed
    """
    serializer_class = UserLocationSerializer
    permission_classes = (IsAdminUser,)
    
    def get(self, request, *args, **kwargs):
        queryset = UserLocationData.objects.all()
        serializer = UserLocationSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = UserLocationSerializer(data=request.data)
        if serializer.is_valid():
            transition_type = int(request.data['transition_type'])
            accuracy = float(request.data['accuracy'])
            if transition_type >= -1 and transition_type <= 4 and \
                    accuracy >= 0.00 and accuracy <= 100.00:
                print "Saving"
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLocationDetails(APIView):
    serializer_class = UserLocationDetailsSerializer
    def get_object(self, uid):
        try:
            return UserLocationData.objects.get(uid=uid)
        except UserLocationData.DoesNotExist:
            raise Http404

    def get(self, request, uid, format=None):
        queryset = self.get_object(uid)
        serializer = UserLocationDetailsSerializer(queryset)
        return Response(serializer.data)


class ListUserLocationDetails(generics.RetrieveAPIView):
    permission_classes = (IsAdminUser,)
    def get(self, request, *args, **kwargs):
        queryset = UserLocationData.objects.all()
        serializer = UserLocationListSerializer(queryset, many=True)
        return Response(serializer.data)
        

class GeofenceViewSet(generics.ListCreateAPIView):
    """
    (Graphical) API endpoint that allows user geofence data  
    to be added or viewed
    """
    serializer_class = GeofenceSerializer
    def get(self, request, *args, **kwargs):
        queryset = Geofence.objects.all()
        serializer = GeofenceGIDSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = GeofenceSerializer(data=request.data)
        if serializer.is_valid():
            expiration_time = int(request.data['expiration_time'])
            if expiration_time > 0:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else: 
                return Response('Error: Expiration time should be valid value')
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GeofenceDetails(APIView):
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

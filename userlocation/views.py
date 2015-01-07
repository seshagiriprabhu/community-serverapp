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

from userlocation.models import Geofence, UserLocationData
from userlocation.serializers import GeofenceSerializer
from userlocation.serializers import GeofenceListSerializer
from userlocation.serializers import GeofenceDetailsSerializer
from userlocation.serializers import GeofenceGIDSerializer
from userlocation.serializers import UserLocationSerializer
from userlocation.serializers import UserLocationListSerializer
from userlocation.serializers import UserLocationDetailsSerializer


class UserLocationViewSet(generics.ListCreateAPIView):
    """
    (Graphical) API endpoint that allows user location data 
    to be added or viewed
    """
    serializer_class = UserLocationSerializer    
    def get(self, request, *args, **kwargs):
        queryset = UserLocationData.objects.all().reverse()[:5]
        serializer = UserLocationListSerializer(queryset, many=True)
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
                return Response(serializer.data,\
                        status=status.HTTP_201_CREATED)
        return Response(serializer.errors,\
                status=status.HTTP_400_BAD_REQUEST)


class UserLocationDetailsViewSet(APIView):
    serializer_class = UserLocationDetailsSerializer
    def get_object(self, email):
        try:
            return UserLocationData.objects.filter(email=email).reverse()
        except UserLocationData.DoesNotExist:
            raise Http404

    def get(self, request, email, format=None):
        queryset = self.get_object(email)
        serializer = UserLocationDetailsSerializer(queryset, many=True)
        return Response(serializer.data)


class UserLocationListViewSet(APIView):
    permission_classes = (IsAdminUser,)
    serializer_class = UserLocationListSerializer
    def get(self, request, *args, **kwargs):
        queryset = UserLocationData.objects.all().reverse()[:10]
        serializer = UserLocationListSerializer(queryset, many=True)
        return Response(serializer.data)
        

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

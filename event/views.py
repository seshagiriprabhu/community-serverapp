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

from event.models import Event, EventAttendance
from event.serializers import EventSerializer
from event.serializers import EventListSerializer
from event.serializers import EventDetailsSerializer
from event.serializers import EventAttendanceSerializer
from event.serializers import EventAttendanceListSerializer
from event.serializers import EventAttendanceDetailsSerializer

from registeration.views import JSONResponse

class EventViewSet(generics.ListCreateAPIView):
    serializer_class = EventSerializer

    def get(self, request ,*args, **kwargs):
        queryset = Event.objects.all()
        serializer = EventListSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            start_time = request.data['start_time']
            end_time = request.data['end_time']
            if end_time > start_time:
                serializer.save()
                return Response(serializer.data,\
                        status=status.HTTP_201_CREATED)
            else:
                return Response(
                        "End time should be greater than start time",\
                        status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.error,\
                    status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.error,\
                status=status.HTTP_400_BAD_REQUEST)


class EventListViewSet(generics.RetrieveAPIView):
    serializer_class = EventListSerializer
    def get(self, request, *args, **kwargs):
        queryset = Event.objects.all()
        serializer = EventListSerializer(queryset, many=True)
        return Response(serializer.data)


class EventDetailsViewSet(APIView):
    serializer_class = EventDetailsSerializer 
    def get_object(self, event_id):
        try:
            return Event.objects.filter(event_id=event_id)
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, event_id, format=None):
        queryset = self.get_object(event_id)
        serializer = EventDetailsSerializer(queryset, many=True)
        return Response(serializer.data)
    

class EventAttendanceViewSet(generics.ListCreateAPIView):
    serializer_class = EventAttendanceSerializer
    def get(self, request, *args, **kwargs):
        queryset = EventAttendance.objects.all()
        serializer = EventAttendanceSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = EventAttendanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventAttendanceListViewSet(APIView):
    serializer_class = EventAttendanceListSerializer
    def get(self, request, *args, **kwargs):
        queryset = EventAttendance.objects.all()
        serializer = EventAttendanceListSerializer(queryset, many=True)
        return Response(serializer.data)


class EventAttendanceDetailsViewSet(generics.RetrieveAPIView):
    serializer_class = EventAttendanceDetailsSerializer
    def get_object(self, event_id):
        try:
            return EventAttendance.objects.filter(event_id=event_id)
        except EventAttendance.DoesNotExist:
            raise Http404

    def get(self, request, event_id, format=None):
        queryset = self.get_object(event_id)
        serializer = EventAttendanceDetailsSerializer(queryset, many=True)
        return Response(serializer.data)


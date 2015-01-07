from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import generics, filters, status, viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from registeration.models import Registeration
from registeration.serializers import RegisterationSerializer
from registeration.serializers import FriendListSerializer
from registeration.serializers import FriendDetailsSerializer
from registeration.serializers import UserListSerializer

from event.models import Event, EventAttendance
from event.serializers import EventDetailsSerializer
from event.serializers import EventAttendanceDetailsSerializer


class RegisteredUserViewSet(generics.ListCreateAPIView):
    """
    (Graphical) API endpoint that allows users to be viewed or added.
    """
    serializer_class = RegisterationSerializer 
    def get(self, request, *args, **kwargs):
        queryset = Registeration.objects.all().reverse()[:5]
        serializer = UserListSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = RegisterationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class FriendListViewSet(APIView):
    serializer_class = FriendListSerializer
    def check_user_exists(self, email):
        try:
            user = Registeration.objects.get(email=email)
            return True
        except Registeration.DoesNotExist:
            return False

    def get(self, request, email, format=None):
        if self.check_user_exists(email):
            queryset = Registeration.objects.all().exclude(email=email)
            serializer = FriendListSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserDetailsViewSet(APIView):
    serializer_class = FriendDetailsSerializer

    def get_object(self, email):
        try:
            return Registeration.objects.get(email=email)
        except Registeration.DoesNotExist:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, email, format=None):
        queryset = self.get_object(email)
        serializer = FriendDetailsSerializer(queryset, many=False)
        return Response(serializer.data)


class UserCreatedEventsViewSet(APIView):
    serializer_class = EventDetailsSerializer
    def get_object(self, email):
        try:
            return Event.objects.filter(event_creator=email)
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, email, format=None):
        queryset = self.get_object(email)
        serializer = EventDetailsSerializer(queryset, many=True)
        return Response(serializer.data)


class UserAttendedEventsViewSet(APIView):
    serializer_class = EventAttendanceDetailsSerializer
    def get_object(self, email):
        try:
            return EventAttendance.objects.filter(\
                    email=email, status='Going')
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, email, format=None):
        queryset = self.get_object(email)
        serializer = EventDetailsSerializer(queryset, many=True)
        return Response(serializer.data)

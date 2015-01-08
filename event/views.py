from rest_framework import generics
from event.models import Event, EventAttendance
from event.serializers import EventSerializer
from event.serializers import EventListSerializer
from event.serializers import EventDetailsSerializer
from event.serializers import EventAttendanceSerializer
from event.serializers import EventAttendanceListSerializer
from event.serializers import EventAttendanceDetailsSerializer


class EventViewSet(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventNameListViewSet(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventDetailsSerializer
    lookup_field =('event_name')


class EventListAllViewSet(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventListSerializer


class EventDetailsViewSet(generics.RetrieveUpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventDetailsSerializer


class EventAttendanceViewSet(generics.ListCreateAPIView):
    queryset = EventAttendance.objects.all()
    serializer_class = EventAttendanceSerializer


class EventAttendanceListViewSet(generics.ListAPIView):
    queryset = EventAttendance.objects.all()
    serializer_class = EventAttendanceListSerializer
    lookup_field = ('event_id')


class EventAttendanceDetailsViewSet(generics.RetrieveUpdateAPIView):
    queryset = EventAttendance.objects.all()
    serializer_class = EventAttendanceDetailsSerializer

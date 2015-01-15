from rest_framework import generics
from datetime import datetime

from event.models import Event, EventAttendance
from event.serializers import EventSerializer
from event.serializers import EventListSerializer
from event.serializers import EventDetailsSerializer
from event.serializers import EventAttendanceSerializer
from event.serializers import EventAttendanceListSerializer
from event.serializers import EventAttendanceDetailsSerializer


class EventViewSet(generics.ListCreateAPIView):
    queryset = Event.objects.all()\
            .order_by('date_time')\
            .reverse()[:5]
    serializer_class = EventSerializer


class EventNameListViewSet(generics.ListAPIView):
    queryset = Event.objects.all()\
            .order_by('date_time')\
            .reverse()
    serializer_class = EventDetailsSerializer
    lookup_field =('event_name')


class EventListAllOpenViewSet(generics.ListAPIView):
    serializer_class = EventListSerializer
    queryset = Event.objects.all().filter(end_time__gte=datetime.now())\
            .order_by('date_time')\
            .reverse()


class EventListAllClosedViewSet(generics.ListAPIView):
    serializer_class = EventListSerializer
    queryset = Event.objects.all().filter(end_time__lte=datetime.now())\
            .order_by('date_time')\
            .reverse()


class EventDetailsViewSet(generics.RetrieveUpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventDetailsSerializer


class EventAttendanceViewSet(generics.ListCreateAPIView):
    queryset = EventAttendance.objects.all()\
            .order_by('date_time')\
            .reverse()[:2]
    serializer_class = EventAttendanceSerializer


class EventAttendanceListViewSet(generics.ListAPIView):
    queryset = EventAttendance.objects.all()\
            .order_by('date_time')\
            .reverse()
    serializer_class = EventAttendanceListSerializer
    lookup_field = ('event_id')


class EventAttendanceDetailsViewSet(generics.RetrieveUpdateAPIView):
    queryset = EventAttendance.objects.all()
    serializer_class = EventAttendanceDetailsSerializer

from rest_framework import generics
from datetime import datetime

from event.models import Event, EventAttendance
from event.serializers import EventSerializer
from event.serializers import EventListSerializer
from event.serializers import EventDetailsSerializer
from event.serializers import EventAttendanceSerializer
from event.serializers import EventAttendanceListSerializer
from event.serializers import EventAttendanceDetailsSerializer


class EventViewSet(generics.CreateAPIView):
    model = Event
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


class EventAttendanceViewSet(generics.CreateAPIView):
    queryset = EventAttendance
    serializer_class = EventAttendanceSerializer


class EventAttendanceListViewSet(generics.ListAPIView):
    serializer_class = EventAttendanceListSerializer
    def get_queryset(self):
        return EventAttendance.objects.all().\
                filter(event_id=self.kwargs['pk'])\
                .order_by('date_time')\
                .reverse()

class EventAttendanceDetailsViewSet(generics.RetrieveUpdateAPIView):
    queryset = EventAttendance.objects.all()
    serializer_class = EventAttendanceDetailsSerializer

from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from registeration.models import Registeration
from registeration.serializers import RegisterationSerializer
from registeration.serializers import FriendListSerializer
from registeration.serializers import FriendDetailsSerializer
from registeration.serializers import UserListSerializer

from event.models import Event, EventAttendance
from event.serializers import EventDetailsSerializer
from event.serializers import EventAttendanceDetailsSerializer


class RegisteredUserViewSet(generics.CreateAPIView):
    model = Registeration

    serializer_class = RegisterationSerializer 


class AllRegisteredUsersViewSet(generics.ListAPIView):
    permissions = (IsAdminUser,)
    queryset = Registeration.objects.all()\
                .order_by('date_time')\
                .reverse()
    serializer_class = RegisterationSerializer


class FriendListViewSet(generics.ListAPIView):
    serializer_class = FriendListSerializer

    def get_queryset(self):
        return Registeration.objects.all()\
                .exclude(email=self.kwargs['pk'])\
                .order_by('date_time')\
                .reverse()


class UserDetailsViewSet(generics.RetrieveUpdateAPIView):
    queryset = Registeration.objects.all()
    serializer_class = FriendDetailsSerializer


class UserCreatedEventsViewSet(generics.ListAPIView):
    serializer_class = EventDetailsSerializer

    def get_queryset(self):
        return Event.objects.all().\
                filter(event_creator=self.kwargs['pk'])\
                .order_by('date_time')\
                .reverse()


class UserAttendedEventsViewSet(generics.ListAPIView):
    serializer_class = EventAttendanceDetailsSerializer

    def get_queryset(self):
        return EventAttendance.objects.all().\
                filter(email=self.kwargs['pk'])\
                .order_by('date_time')\
                .reverse()

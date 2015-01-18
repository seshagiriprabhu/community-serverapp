from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from datetime import datetime, timedelta

from userlocation.models import UserLocationData
from userlocation.serializers import UserLocationSerializer
from userlocation.serializers import UserLocationListSerializer
from userlocation.serializers import UserLocationDetailsSerializer


class UserLocationViewSet(generics.ListCreateAPIView):
    queryset = UserLocationData.objects.all()\
            .order_by('date_time')\
            .reverse()[:5]
    serializer_class = UserLocationSerializer    


class UserLocationDetailsViewSet(generics.RetrieveAPIView):
    queryset = UserLocationData.objects.all()
    serializer_class = UserLocationDetailsSerializer


class UserLocationListViewSet(generics.ListAPIView):
    permission_classes = (IsAdminUser,)
    queryset = UserLocationData.objects.all()\
            .order_by('date_time')\
            .reverse()
    serializer_class = UserLocationListSerializer


class GeofenceUserActivitiesViewSet(generics.ListAPIView):
    serializer_class = UserLocationListSerializer
    lookup_field = ('gid')
    queryset = UserLocationData.objects\
            .filter(transition_type__lte=2,\
            date_time__gte = datetime.now() - timedelta(days=1))\
            .exclude(transition_type__lte=-1)\
            .order_by('date_time')\
            .reverse()

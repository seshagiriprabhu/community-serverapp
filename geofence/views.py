from rest_framework import generics
from geofence.models import Geofence
from geofence.serializers import GeofenceSerializer
from geofence.serializers import GeofenceListSerializer
from geofence.serializers import GeofenceDetailsSerializer
from geofence.serializers import GeofenceGIDSerializer


class GeofenceViewSet(generics.CreateAPIView):
    queryset = Geofence
    serializer_class = GeofenceSerializer


class GeofenceListViewSet(generics.ListAPIView):
    queryset = Geofence.objects.all()\
            .order_by('date_time')\
            .reverse()
    serializer_class = GeofenceListSerializer


class GeofenceNameSearchDetailsViewset(generics.ListAPIView):
    serializer_class = GeofenceSerializer
    def get_queryset(self):
        return Geofence.objects\
                .filter(fence_name=self.kwargs['pk'])\
                .order_by('date_time')\
                .reverse()


class GeofenceDetailsViewSet(generics.RetrieveUpdateAPIView):
    queryset = Geofence.objects.all()
    serializer_class = GeofenceDetailsSerializer

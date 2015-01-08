from rest_framework import generics
from geofence.models import Geofence
from geofence.serializers import GeofenceSerializer
from geofence.serializers import GeofenceListSerializer
from geofence.serializers import GeofenceDetailsSerializer
from geofence.serializers import GeofenceGIDSerializer


class GeofenceViewSet(generics.ListCreateAPIView):
    queryset = Geofence.objects.all().reverse()[:5]
    serializer_class = GeofenceSerializer


class GeofenceListViewSet(generics.ListAPIView):
    queryset = Geofence.objects.all().reverse()
    serializer_class = GeofenceListSerializer


class GeofenceNameSearchDetailsViewset(generics.ListAPIView):
    serializer_class = GeofenceSerializer
    def get_queryset(self):
        return Geofence.objects\
                .filter(fence_name=self.kwargs['pk'])\
                .reverse()


class GeofenceDetailsViewSet(generics.RetrieveUpdateAPIView):
    queryset = Geofence.objects.all()
    serializer_class = GeofenceDetailsSerializer

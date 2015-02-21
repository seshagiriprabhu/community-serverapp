from rest_framework import serializers
from django.forms import widgets
from geofence.models import Geofence


class GeofenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geofence
        fields = ('fence_name', 'latitude', 'longitude',\
                'geofence_radius', 'email')

    def create(self, validated_data):
        return Geofence.objects.create(**validated_data)


class GeofenceGIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geofence
        fields = ('gid', 'fence_name')


class GeofenceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geofence
        fields = ('gid', 'fence_name', 'latitude', 'longitude',\
                'geofence_radius', 'email')


class GeofenceDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geofence
        fields = ('gid', 'fence_name', 'latitude', 'longitude',\
                'geofence_radius', 'expiration_time', 'email',\
                'date_time')

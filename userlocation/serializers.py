from rest_framework import serializers
from django.forms import widgets
from userlocation.models import Geofence, UserLocationData

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
        fields = ('gid', 'fence_name')


class GeofenceDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geofence
        fields = ('gid', 'fence_name', 'latitude', 'longitude',\
                'geofence_radius', 'expiration_time', 'email',\
                'created_date_time')


class UserLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLocationData
        fields = ('email', 'accuracy', 'transition_type', 'gid')

    def create(self, validated_data):
        return UserLocationData.objects.create(**validated_data)


class UserLocationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLocationData
        fields = ('date_time', 'email')


class UserLocationDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLocationData
        fields = ('email', 'date_time', 'accuracy',\
                'transition_type', 'gid')

from rest_framework import serializers
from django.forms import widgets
from userlocation.models import Geofence, UserLocationData, UserPhoneData
from userlocation.models import BATTERY_STATE, CONNECTION_METHOD

class GeofenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geofence
        fields = ('fence_name', 'latitude', 'longitude',\
                'geofence_radius', 'expiration_time',\
                'email')

    def create(self, validated_data):
        return Geofence.objects.create(**validated_data)


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


class UserLocationDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLocationData
        fields = ('uid', 'email', 'date_time', 'accuracy',\
                'transition_type', 'gid')

    
class UserPhoneDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPhoneData
        fields = ('email', 'date_time', 'battery_state',\
                'app_power_consumption', 'avg_mem_util',\
                'avg_cpu_util', 'last_online_time',\
                'last_online_duration', 'connection_method',\
                'app_data_transfered')

    def create(self, validated_data):
        return UserPhoneData.objects.create(**validated_data)

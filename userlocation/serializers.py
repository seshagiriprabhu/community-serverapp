from rest_framework import serializers
from django.forms import widgets
from userlocation.models import Geofence, UserLocationData, UserPhoneData
from userlocation.models import BATTERY_STATE, CONNECTION_METHOD

class GeofenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geofence
        fields = ('gid', 'latitude', 'longitude', 'geofence_radius',\
                'expiration_time', 'email')

    def create(self, validated_data):
        return Geofence.objects.create(**validated_data)


class UserLocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserLocationData
        fields = ('email', 'accuracy', 'date_time',\
                'transition_type', 'geofence_id')

    def create(self, validated_data):
        return UserLocationData.objects.create(**validated_data)

    
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


class GeofenceFullDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geofence
        fields = ('gid', 'latitude', 'longitude', 'geofence_radius',\
                'expiration_time', 'email', 'date_time')


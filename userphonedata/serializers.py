from rest_framework import serializers
from django.forms import widgets
from userphonedata.models import UserPhoneData

    
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


class UserPhoneDataListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPhoneData
        fields = ('uid', 'date_time', 'email')


class UserPhoneDataDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPhoneData
        fields = ('uid', 'email', 'date_time', 'battery_state',\
                'app_power_consumption', 'avg_mem_util',\
                'avg_cpu_util', 'last_online_time',\
                'last_online_duration', 'connection_method',\
                'app_data_transfered')

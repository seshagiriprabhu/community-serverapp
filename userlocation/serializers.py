from rest_framework import serializers
from django.forms import widgets
from userlocation.models import UserLocationData


class UserLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLocationData
        fields = ('email', 'date_time',\
                'accuracy', 'transition_type', 'gid')

    def create(self, validated_data):
        return UserLocationData.objects.create(**validated_data)


class UserLocationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLocationData
        fields = ('email', 'date_time',\
                'accuracy', 'transition_type', 'gid')


class UserLocationDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLocationData
        fields = ('email', 'date_time', 'accuracy',\
                'transition_type', 'gid')

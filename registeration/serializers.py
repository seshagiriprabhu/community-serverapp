from rest_framework import serializers
from django.forms import widgets
from registeration.models import Registeration

class DateTimeTzAwareField(serializers.DateTimeField):
    def to_native(self, value):
        value = timezone.localtime(value)
        return super(DateTimeTzAwareField, self).to_native(value)


class RegisterationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registeration
        fields = ('display_name', 'email', 'gender', 'date_of_birth',\
                'phone_number', 'mobile_os', 'mobile_device', 'phone_uid',\
                'carrier')
    
    def create(self, validated_data):
        return Registeration.objects.create(**validated_data)


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registeration
        fields = ('display_name', 'email')


class FriendListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registeration
        fields = ('display_name', 'email', 'gender', 'date_of_birth', \
                'phone_number')


class FriendDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registeration
        fields = ('display_name', 'email', 'gender', 'date_of_birth',\
                'phone_number')

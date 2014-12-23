from rest_framework import serializers
from django.forms import widgets
from registeration.models import Registeration, GENDER_CHOICES

class RegisterationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Registeration
        fields = ('display_name', 'email', 'gender', 'date_of_birth',\
                'phone_number', 'mobile_os', 'mobile_device', 'phone_uid',\
                'carrier')
    
    def create(self, validated_data):
        return Registeration.objects.create(**validated_data)


class FriendListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Registeration
        fields = ('display_name', 'email')


class FriendDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Registeration
        fields = ('display_name', 'email', 'gender', 'date_of_birth',\
                'phone_number')

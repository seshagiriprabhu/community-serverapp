from rest_framework import serializers
from django.forms import widgets
from event.models import Event, EventAttendance
from registeration.serializers import DateTimeTzAwareField


class EventSerializer(serializers.ModelSerializer):
    start_time = DateTimeTzAwareField()
    end_time = DateTimeTzAwareField()
    class Meta:
        model = Event
        fields = ('event_name', 'event_description',\
                'event_creator', 'personal_feeling', 'start_time',\
                'end_time', 'geofence_id')

    def create(self, validated_data):
        return Event.objects.create(**validated_data)


class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('event_id', 'event_name', 'event_description',\
                'event_creator', 'personal_feeling', 'start_time',\
                'end_time', 'geofence_id')


class EventDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('event_id', 'event_name', 'event_description',\
                'event_creator', 'personal_feeling', 'start_time',\
                'end_time', 'geofence_id')


class EventAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventAttendance
        fields = ('aid', 'event_id', 'email', 'status')

    def create(self, validated_data):
        return EventAttendance.objects.create(**validated_data)


class EventAttendanceListSerializer(serializers.ModelSerializer): 
    class Meta:
        model = EventAttendance
        fields = ('aid', 'email', 'display_name', 'status')


class EventAttendanceDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventAttendance
        fields = ('aid', 'email', 'display_name', 'status')

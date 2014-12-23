from rest_framework import serializers
from django.forms import widgets
from event import Event, EventAttendance

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('event_id', 'event_name', 'event_description',\
                'event_creator', 'personal_feeling', 'start_time'\
                'end_time', 'geofence_id')

    def create(self, validated_data):
        return Event.objects.create(**validated_data)

class EventAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model=EventAttendance
        fields = ('id', 'event_id', 'email', 'display_name')

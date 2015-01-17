from django.db import models
from datetime import datetime
from django.utils import timezone

from geofence.models import Geofence
from registeration.models import Registeration, AutoDateTimeField

GOING_STATUS = (
                ('Going', 'Going'),
                ('May be', 'May be'), 
                ('Not going', 'Not Going')
)


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=128,\
            blank=False)
    event_description = models.CharField(max_length=2048, blank=True)
    event_creator = models.ForeignKey(Registeration,\
            related_name='event')
    personal_feeling = models.CharField(max_length=32, blank=True)
    start_time = models.DateTimeField(blank=False)
    end_time = models.DateTimeField(blank=False)
    geofence_id = models.ForeignKey(Geofence)
    date_time = models.DateTimeField(default=timezone.now, blank=True,\
            editable=False, verbose_name="event created time")
    modified_time = AutoDateTimeField(default=timezone.now,\
            blank=False, verbose_name="Last Modified time")

    def create(self, validated_data):
        return Event.objects.create(**validated_data)

    def save(self, *args, **kwargs):
        super(Event, self).save(*args, **kwargs)

    class Meta:
        db_table = 'event'
        ordering = ('event_id', 'event_creator',)

    def __unicode__(self):
        return self.event_name


class EventAttendance(models.Model):
    aid = models.AutoField(primary_key=True)
    event_id = models.ForeignKey(Event,\
            verbose_name='Event name',\
            related_name='attendees')
    email = models.ForeignKey(Registeration)
    display_name = models.CharField(blank=True,\
            max_length=32)
    status = models.CharField(max_length=10, choices=GOING_STATUS) 
    date_time = models.DateTimeField(default=timezone.now,\
            blank=False, editable=False)
    modified_time = AutoDateTimeField(default=timezone.now,\
            blank=False, verbose_name="Last Modified time")

    def create(self, validated_data):
        return EventAttendance.objects.create(**validated_data)

    def save(self, *args, **kwargs):
        user_data = Registeration.objects.get(email=self.email)
        self.display_name = user_data.display_name
        super(EventAttendance, self).save(*args, **kwargs)

    class Meta:
        db_table = 'event_attendance'
        unique_together = (('event_id', 'email'))
        ordering = ('aid', 'event_id',)

    def __unicode__(self):
        return self.aid

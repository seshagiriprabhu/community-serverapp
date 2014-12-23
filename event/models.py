from django.db import models
from registeration.models import Registeration
from userlocation.models import Geofence

class Event(models.Model):
    event_id = models.CharField(max_length=32, primary_key=True)
    event_name = models.CharField(max_length=128, blank=False)
    event_description = models.CharField(max_length=2048, blank=True)
    event_creator = models.ForeignKey(Registeration)
    personal_feeling = models.CharField(max_length=32, blank=True)
    start_time = models.DateTimeField(blank=False)
    end_time = models.DateTimeField(blank=False)
    geofence_id = models.ForeignKey(Geofence)

class EvenAttendance(models.Model):
    id = models.AutoField(primary_key=True)
    event_id = models.ForeignKey(Event)
    email = models.ForeignKey(Registeration)
    display_name = models.CharField(blank=False, max_length=32, unique=True)


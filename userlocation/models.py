from django.db import models
from registeration.models import Registeration
import hashlib

BATTERY_STATE = (
        ('P', 'Plugged'), 
        ('B', 'Battery')
)

CONNECTION_METHOD = (
        ('1', '2G'),
        ('2', '2G'),
        ('3', '3G'),
        ('4', '4G')
)

class Geofence(models.Model):
    gid = models.AutoField(primary_key=True)
    latitude = models.DecimalField(
            max_digits=9, decimal_places=2, blank=False)
    longitude = models.DecimalField(
            max_digits=9, decimal_places=2, blank=False)
    geofence_radius = models.DecimalField(
            max_digits=9, decimal_places=2, blank=False)
    expiration_time = models.IntegerField(blank=False)
    email = models.ForeignKey(Registeration)
    date_time = models.DateTimeField(auto_now_add=True, blank=True)

    def save(self, *args, **kwargs):
        super(Geofence, self).save(*args, **kwargs)

    class Meta:
        db_table = 'geofence'
        ordering = ('latitude', 'longitude', 'geofence_radius',\
                'expiration_time', 'email')

    def __unicode__(self):
        return self.gid


class UserLocationData(models.Model):
    uid = models.CharField(primary_key=True, max_length=32)
    email = models.ForeignKey(Registeration)
    accuracy = models.DecimalField(max_digits=3, decimal_places=2)
    date_time = models.DateTimeField(auto_now_add=True, blank=True)
    transition_type = models.IntegerField(blank=False)
    geofence_id = models.ForeignKey(Geofence)

    def save(self, *args, **kwargs):
        hash_elements = str(email) + str(date_time)
        self.uid = hashlib.md5.new(hash_elements).digest()
        super(UserLocationData, self).save(*args, **kwargs)

    class Meta:
        db_table = 'user_location_data'
        ordering = ('email', 'accuracy', 'date_time',\
                'transition_type', 'geofence_id')

    def __unicode__(self):
        return self.uid


class UserPhoneData(models.Model):
    uid = models.CharField(primary_key=True, max_length=32)
    email = models.ForeignKey(Registeration)
    date_time = models.DateTimeField(auto_now_add=True, blank=True)
    batter_state = models.CharField(
            max_length=1, blank=False, choices=BATTERY_STATE)
    app_power_consumption = models.DecimalField(
            max_digits=3, decimal_places=2, blank=False)
    avg_mem_util = models.DecimalField(
            max_digits=3, decimal_places=2, blank=False)
    avg_cpu_util = models.DecimalField(
            max_digits=3, decimal_places=2, blank=False)
    last_online_time = models.DateTimeField(blank=False)
    last_online_duration = models.DecimalField(
            blank=False, max_digits=10, decimal_places=2)
    connection_method = models.CharField(
            max_length=1, blank=False, choices=CONNECTION_METHOD)
    app_data_transfered = models.DecimalField(
            blank=False, max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        hash_elements = str(email) + str(date_time)
        self.uid = hashlib.md5.new(hash_elements).digest()
        super(Model, self).save(*args, **kwargs)

    class Meta:
        db_table = 'user_phone_data'
        ordering = ('email', 'date_time',)

    def __unicode__(self):
        return self.uid

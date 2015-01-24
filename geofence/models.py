from django.db import models
from django.utils import timezone
from registeration.models import Registeration
from djgeojson.fields import PointField

class Geofence(models.Model):
    gid = models.AutoField(primary_key=True)
    fence_name = models.CharField(max_length=256, blank=False)
    latitude = models.DecimalField(
            max_digits=9, decimal_places=6, blank=False)
    longitude = models.DecimalField(
            max_digits=9, decimal_places=6, blank=False)
    geofence_radius = models.DecimalField(
            max_digits=9, decimal_places=2, blank=False)
    expiration_time = models.IntegerField(blank=True)
    email = models.ForeignKey(Registeration)
    date_time = models.DateTimeField(default=timezone.now, \
            editable=False, blank=True)
    
    def create(self, validated_data):
        return Geofence.objects.create(**validated_data)

    def save(self, *args, **kwargs):
        # Expiration time of geofence is set as never expire
        self.expiration_time = -1 
        super(Geofence, self).save(*args, **kwargs)

    class Meta:
        db_table = 'geofence'
        ordering = ('gid', 'fence_name', 'latitude', 'longitude',\
                'geofence_radius', 'email')

    def __unicode__(self):
        return u'%s, %s' % (self.gid, self.fence_name)

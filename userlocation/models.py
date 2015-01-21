from django.db import models
from django.utils import timezone

from geofence.models import Geofence
from registeration.models import Registeration


class UserLocationData(models.Model):
    uid = models.AutoField(primary_key=True)
    email = models.ForeignKey(Registeration)
    accuracy = models.DecimalField(max_digits=5, decimal_places=2)
    date_time = models.DateTimeField(blank=False)
    transition_type = models.IntegerField(blank=False)
    gid = models.ForeignKey(Geofence, verbose_name="Geofence")
    
    def create(self, validated_data):
        self.date_time = timezone(self.date_time).make_aware()
        return UserLocationData.objects.create(**validated_data)

    def save(self, *args, **kwargs):
        super(UserLocationData, self).save(*args, **kwargs)

    class Meta:
        db_table = 'user_location_data'
        ordering = ('email', 'date_time', 'accuracy',\
                'transition_type', 'gid')

    def __unicode__(self):
        return self.uid



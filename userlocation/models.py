from django.db import models
from registeration.models import Registeration
from geofence.models import Geofence

class UserLocationData(models.Model):
    uid = models.AutoField(primary_key=True)
    email = models.ForeignKey(Registeration)
    accuracy = models.DecimalField(max_digits=5, decimal_places=2)
    date_time = models.DateTimeField(auto_now_add=True, blank=True,\
            verbose_name="Uploaded time")
    transition_type = models.IntegerField(blank=False)
    gid = models.ForeignKey(Geofence, verbose_name="Geofence")
    
    def create(self, validated_data):
        return UserLocationData.objects.create(**validated_data)

    def save(self, *args, **kwargs):
        super(UserLocationData, self).save(*args, **kwargs)

    class Meta:
        db_table = 'user_location_data'
        ordering = ('email', 'accuracy', 'transition_type', 'gid')

    def __unicode__(self):
        return self.uid



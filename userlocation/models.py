from django.db import models
from django.utils import timezone
from django.contrib.gis.geos import Point
from geofence.models import Geofence
from registeration.models import Registeration
from dataonmap.models import UserGeoLocation

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
        current_gid = str(self.gid).partition(',')[0]
        geofence = Geofence.objects.get(gid=current_gid)
        userdata = Registeration.objects.get(email=self.email)
        UserGeoLocation(disp_name=userdata.display_name,\
                date_time=self.date_time,\
                t_type=self.transition_type,\
                fence_name = geofence.fence_name,\
                geom=Point(
                float(geofence.longitude),\
                float(geofence.latitude))).save()
        super(UserLocationData, self).save(*args, **kwargs)

    class Meta:
        db_table = 'user_location_data'
        ordering = ('email', 'date_time', 'accuracy',\
                'transition_type', 'gid')

    def __unicode__(self):
        return self.uid



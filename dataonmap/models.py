from django.contrib.gis.db import models
from django.contrib.gis import admin
from registeration.models import Registeration

class UserGeoLocation(models.Model):
    disp_name = models.CharField(max_length=32)
    date_time = models.DateTimeField()
    t_type = models.IntegerField()
    fence_name = models.CharField(max_length=128)
    geom = models.PointField(srid=4326)

    def __unicode__(self):
        return self.disp_name


class GeofenceMap(models.Model):
    gid = models.IntegerField()
    fence_name = models.CharField(max_length=128)
    geom = models.PointField()

    def __unicode__(self):
        return self.disp_name


admin.site.register(UserGeoLocation, admin.OSMGeoAdmin)

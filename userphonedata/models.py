from django.db import models
from registeration.models import Registeration

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

class UserPhoneData(models.Model):
    uid = models.AutoField(primary_key=True)
    email = models.ForeignKey(Registeration)
    date_time = models.DateTimeField(auto_now_add=True, blank=True)
    battery_state = models.CharField(
            max_length=1, blank=False, choices=BATTERY_STATE)
    app_power_consumption = models.DecimalField(
            max_digits=5, decimal_places=2, blank=False)
    avg_mem_util = models.DecimalField(
            max_digits=5, decimal_places=2, blank=False)
    avg_cpu_util = models.DecimalField(
            max_digits=5, decimal_places=2, blank=False)
    last_online_time = models.DateTimeField(blank=False)
    last_online_duration = models.DecimalField(
            blank=False, max_digits=10, decimal_places=2)
    connection_method = models.CharField(
            max_length=1, blank=False, choices=CONNECTION_METHOD)
    app_data_transfered = models.DecimalField(
            blank=False, max_digits=10, decimal_places=2)

    def create(self, validated_data):
        return UserPhoneData.objects.create(**validated_data)

    def save(self, *args, **kwargs):
        super(UserPhoneData, self).save(*args, **kwargs)

    class Meta:
        db_table = 'user_phone_data'
        ordering = ('email', 'date_time',)

    def __unicode__(self):
        return self.uid

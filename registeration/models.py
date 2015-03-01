from django.db import models
from datetime import datetime
from django.utils import timezone

GENDER_CHOICES = (
        ('M', 'Male'), 
        ('F', 'Female'), 
        ('A', 'Anonymous')
)

class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return datetime.now()


class Registeration(models.Model):
    email = models.EmailField(primary_key=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(
            max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    display_name = models.CharField(
            max_length=32, blank=False, unique=True)
    date_time = models.DateTimeField(default=timezone.now,\
            editable=False, blank=True)
    password = models.CharField(max_length=128, blank=False)
    phone_number = models.CharField(max_length=11, blank=True)
    mobile_os = models.CharField(max_length=100, blank=True)
    mobile_device = models.CharField(max_length=100, blank=True)
    phone_uid = models.CharField(max_length=100, blank=True)
    carrier = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        super(Registeration, self).save(*args, **kwargs)

    class Meta:
        db_table = 'user_details'
        ordering = ('display_name', 'email', 'password',\
                'date_of_birth', 'gender')

    def __unicode__(self):
        return self.email


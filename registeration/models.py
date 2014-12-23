from django.db import models
import md5

GENDER_CHOICES = (
        ('M', 'Male'), 
        ('F', 'Female'), 
        ('A', 'Anonymous')
)

class Registeration(models.Model):
    email = models.EmailField(primary_key=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(
            max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    display_name = models.CharField(
            max_length=32, blank=False, unique=True)
    date_time = models.DateTimeField(auto_now_add=True, blank=True)
    phone_number = models.CharField(max_length=11, blank=True)
    mobile_os = models.CharField(max_length=100, blank=False)
    mobile_device = models.CharField(max_length=100, blank=False)
    phone_uid = models.CharField(max_length=100, blank=False)
    carrier = models.CharField(max_length=100, blank=False)

    def save(self, *args, **kwargs):
        super(Registeration, self).save(*args, **kwargs)

    class Meta:
        db_table = 'user_details'
        ordering = ('display_name', 'email', 'date_of_birth', 'gender')

    def __unicode__(self):
        return self.email


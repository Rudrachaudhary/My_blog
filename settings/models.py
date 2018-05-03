from django.db import models

# Create your models here.
class Setting(models.Model):
    site_name = models.CharField(max_length=240)
    contact_number = models.CharField(max_length=240)
    contact_email = models.CharField(max_length=240)
    address = models.CharField(max_length=240)

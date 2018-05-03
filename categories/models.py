from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
     name = models.CharField(max_length=240)
     timestamps = models.DateTimeField(auto_now_add=True)
     #def get_absolute_url(self):
        #return reverse('categories', kwargs={'pk': self.pk})

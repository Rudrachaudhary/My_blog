from django.db import models

# Create your models here.
class Tag(models.Model):
    tag = models.CharField(max_length=240)
    #posts = models.ManyToManyField(Post)
    timestamps = models.DateTimeField(auto_now_add=True)
    #def get_absolute_url(self):
       #return reverse('categories', kwargs={'pk': self.pk})

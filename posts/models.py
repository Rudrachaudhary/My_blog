from django.db import models
from django.urls import reverse
from categories.models import Category
from tags.models import Tag
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=240)
    content = models.TextField(verbose_name='content', null=True,)
    featured = models.FileField(upload_to='documents/')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    timestamps = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category
    #def get_absolute_url(self):
        #return reverse('post-detail', kwargs={'pk': self.pk})
    def save(self,*args,**kwargs):
        self.tags = self.tags.tag

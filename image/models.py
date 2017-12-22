from django.db import models
from django.contrib.auth.models import User
from slugify import slugify

class ImageModel(models.Model):
    image = models.ImageField()
    user = models.ForeignKey(User,related_name='image',on_delete=models.CASCADE)
    url = models.URLField(blank=True)
    slug = models.SlugField(max_length=200,blank=True)
    desc = models.TextField()
    title = models.CharField(max_length=200)
    pub = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(ImageModel,self).save(*args,**kwargs)

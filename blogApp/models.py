from django.db import models
import imp
from django.utils.text import slugify

# Create your models here.
from django.utils import timezone
class Models(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200,primary_key=True,unique=True)
    content=models.TextField()
    publishAT=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title+''+str(self.publishAT.strftime('%d-%m-%Y %H:%M'))
from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField(null=True,blank=True)
    demo_link = models.Charfield(max_length=2000,null=True,blank=True)
    source_link = models.CharField(max_length=2000,null=True,blank=True)

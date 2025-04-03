from django.db import models


# Create your models here.
class student(models.Model):
    sno = models.IntegerField()
    sname = models.CharField(max_length=30)
    branch = models.CharField(max_length=20)
    saddr = models.CharField(max_length=20)



    

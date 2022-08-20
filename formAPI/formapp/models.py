from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=25)
    std = models.IntegerField()
    gender = models.CharField(max_length=10)
    address = models.TextField()
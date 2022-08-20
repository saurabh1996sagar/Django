from unicodedata import category
from django.db import models
from django.shortcuts import render
from datetime import datetime

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=25)
    category = models.CharField(max_length=25)
    description = models.TextField()
    created_at = models.DateTimeField(default=datetime.now())
    author = models.CharField(max_length=20,default='Admin')

    def __str__(self) :
        return f"{self.id} - {self.category}"
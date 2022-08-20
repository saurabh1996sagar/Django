from datetime import datetime
from unicodedata import category
from django.db import models
from datetime import datetime
# Create your models here.
class Blog(models.Model):
    tittle = models.CharField(max_length=25)
    category = models.CharField(max_length=25)
    description = models.TextField()
    created_at  =models.DateTimeField(default=datetime.now())
    author = models.CharField(max_length=25, default='ADMIN')
    
    def __str__(self) -> str:
        return self.tittle
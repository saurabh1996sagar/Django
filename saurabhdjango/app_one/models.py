from django.db import models

# Create your models here.
class Form(models.Model):
    Form_name = models.CharField(max_length=20)
    age = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return self.Form_name
        
from django.db import models

# Create your models here.
class Employee(models.Model):
    Employee_id = models.IntegerField()
    Employee_name = models.CharField(max_length=25)
    Address = models.TextField()

    def __str__(self) -> str:
        return self.Employee_name
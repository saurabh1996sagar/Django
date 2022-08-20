from django.db import models

# Create your models here.
class Employee(models.Model):
    Employee_id = models.IntegerField()
    Employee_name  = models.CharField(max_length=25)
    address = models.TextField()

    def __str__(self):
        return self.Employee_name

class Department(models.Model):
    Department_id = models.IntegerField()
    Department_name  = models.CharField(max_length=25)
    Number = models.IntegerField()

    def __str__(self):
        return self.Department_name     

class Student(models.Model):
    Student_name = models.CharField(max_length=25)           
    age = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return self.Student_name
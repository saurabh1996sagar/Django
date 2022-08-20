from ctypes import addressof
from django.db import models

# Create your models here.

class Faculty(models.Model):
    faculty_name = models.CharField(max_length=25)
    qualification = models.CharField(max_length=25)
    salary = models.IntegerField()

    def __str__(self):
        return self.faculty_name

class Student(models.Model):
    student_name = models.CharField(max_length=25)
    age = models.IntegerField(default='10')
    address = models.TextField()

    def __str__(self):
        return self.student_name +','+self.address
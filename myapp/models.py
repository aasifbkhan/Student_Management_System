from django.db import models

# Create your models here.

#--------------------------------------------Student Model--------------------------------------------
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contact = models.CharField(max_length=10)
    email = models.EmailField()
    course = models.CharField(max_length=20)
    fees = models.FloatField()

class Course(models.Model):
    course = models.CharField(max_length=20)
    fees = models.FloatField()

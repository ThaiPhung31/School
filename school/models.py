from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()


class Class(models.Model):
    name = models.CharField(max_length=50)
    school=models.ForeignKey(School, on_delete=models.CASCADE)

class Student(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    

from django.db import models

# Create your models here.

class Stud(models.Model):
    Reg=models.IntegerField()
    Name=models.CharField(max_length=30)
    Class=models.IntegerField()
    Section=models.CharField(max_length=30)
    Rollno=models.IntegerField()
    Gender=models.CharField(max_length=30)
    Percentage=models.CharField(max_length=30)
    Phone=models.IntegerField()
    Address=models.CharField(max_length=30)
    

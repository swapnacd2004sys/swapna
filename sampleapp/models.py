from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    usertype=models.CharField(max_length=50)
    address=models.CharField(max_length=255,null=True)
    phone_number= models.IntegerField(null=True)

class Teacher(models.Model):
    teacher_id=models.ForeignKey(User,on_delete=models.CASCADE)
    experience=models.IntegerField(null=True)
    salary=models.IntegerField(null=True)

class Student(models.Model):
    Student_id=models.ForeignKey(User,on_delete=models.CASCADE)
    guardian=models.CharField(max_length=30)
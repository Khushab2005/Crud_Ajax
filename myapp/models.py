from django.db import models
from myapp.constant import *
# Create your models here.


class Employe(models.Model):
    images = models.ImageField(upload_to='IMAGES/Employe_profile/')
    name = models.CharField(max_length=255,blank=False,null=False)
    email = models.EmailField(unique=True,blank=False,null=False)
    gender = models.CharField(max_length=255,blank=False,null=False,choices=GENDER_CHOICE)
    department = models.CharField(choices=DEPARTMENT_CHOICE,blank=False,null=False,max_length=255)


 
    def __str__(self):
        return f"{self.name} -  {self.email}"
    
from django.db import models

# Create your models here.


class CVData(models.Model):
    name = models.CharField(max_length=30)
    email =models.EmailField(max_length=250)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=500)
    website = models.CharField(max_length=200,blank=True,null=True)
    photo = models.ImageField(blank=True,null=True)
    edu_qualification = models.CharField(max_length=500)
    skills = models.CharField(max_length=100)


    

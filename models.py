from django.db import models
from django.contrib.auth.models import User 


# Create your models here.
class user_profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null= True, blank = False)
    name = models.CharField(max_length=200, blank=True, null=True)
    headline = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(null=True, blank=True, default= False,editable=True)
    certificates = models.ImageField(default=False , editable= True)
    bio = models.TextField(max_length=1000,default = True,null = True)
    skills = models.TextField(max_length=1000, blank=True, null=True)
    mobile = models.BigIntegerField(default=True,null = True)
    location= models.CharField(default = True,max_length=200)
    social_github = models.CharField(max_length=200, blank=True, null=True)
    social_linkedin = models.CharField(max_length=200, blank=True, null=True)
    social_website = models.CharField(max_length=200, blank=True, null=True)
    resume  = models.FileField(default = False,null = True)


    


from datetime import date
from distutils.command.upload import upload
from email.policy import default
from django.db import models

# Create your models here.
class Register(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100)
    city_or_location = models.CharField(max_length=100)
    Applying_for_Expertise = models.CharField(max_length=100)
    current_or_last_organization = models.CharField(max_length=100)
    Years_of_experience = models.CharField(max_length=100,null=True,default=None)
    LinkedIn_Profile_Page_URL = models.CharField(max_length=100,null=True,default=None)
    EP_no = models.CharField(max_length=100,null=True,default=None)
    resume = models.FileField(max_length=500,null=True,default=None)

    def __str__(self):
        return self.first_name





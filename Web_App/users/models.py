from django.db import models
from django.contrib.auth.models import User

class Userdata(models.Model):
    user = models.OneToOneField(User)
    email = models.CharField(max_length=40, unique=True)
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    phone = models.CharField(max_length=10, unique=True)
    address = models.TextField()
    dob = models.DateTimeField('Date of Birth')
 

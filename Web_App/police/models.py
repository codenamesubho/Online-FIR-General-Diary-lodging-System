from django.db import models
from django.contrib.auth.models import User

class Stationdata(models.Model):
    user = models.OneToOneField(User)
    StationCode = models.CharField(max_length=8,default="00000000")
    StationName = models.CharField(max_length=500)
    Incharge = models.CharField(max_length=40)
    State = models.CharField(max_length=50)
    District = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    address = models.TextField()
 
    def __str__(self):              # __unicode__ on Python 2
        return self.StationCode
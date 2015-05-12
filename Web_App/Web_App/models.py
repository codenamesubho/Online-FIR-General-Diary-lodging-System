from django.db import models
from django.contrib.auth.models import User
from police.models import Stationdata

class general_diary(models.Model):
    ref_id = models.CharField(max_length=40,unique=True,default="00000")
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    mobile = models.CharField(max_length=10)
    email = models.CharField(max_length=80)
    address = models.TextField()
    DOB = models.DateField('date of birth')
    idType_1 = models.CharField(max_length=10)
    idType_1_value = models.CharField(max_length=15)
    idType_2 = models.CharField(max_length=20)
    idType_2_value = models.CharField(max_length=15)

    StationCode = models.ForeignKey(Stationdata)
    Subject = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    detail = models.TextField()
    Time = models.DateTimeField('Occurence')
    Place = models.CharField(max_length=200)
    Loss = models.CharField(max_length=200)
    OTP = models.BooleanField(default=False)
    def __str__(self):              # __unicode__ on Python 2
        return self.Subject

class Fir(models.Model):
    ref_id = models.CharField(max_length=40,unique=True,default="00000")
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    mobile = models.CharField(max_length=10)
    email = models.CharField(max_length=80)
    address = models.TextField()
    DOB = models.DateField('date of birth')
    idType_1 = models.CharField(max_length=10)
    idType_1_value = models.CharField(max_length=15)
    idType_2 = models.CharField(max_length=20)
    idType_2_value = models.CharField(max_length=15)

    StationCode = models.ForeignKey(Stationdata)
    Subject = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    detail = models.TextField()
    Suspect = models.CharField(max_length=500)
    Time = models.DateTimeField('Occurence')
    Place = models.CharField(max_length=200)
    Witness = models.CharField(max_length=500)
    Loss = models.CharField(max_length=200)
    OTP = models.BooleanField(default=False)

    def __str__(self):              # __unicode__ on Python 2
        return self.Subject

class lookup_table(models.Model):
    ref_id = models.CharField(max_length=40,unique=True,default="00000")
    hashmap = models.CharField(max_length=70,unique=True,default="00000")
    type = models.CharField(max_length=5,default="GD")

    def __str__(self):              # __unicode__ on Python 2
        return self.hashmap
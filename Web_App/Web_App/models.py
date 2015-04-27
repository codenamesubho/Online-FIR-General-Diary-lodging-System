from django.db import models
from django.contrib.auth.models import User
from police.models import Stationdata

class General_Diary(models.Model):
    lodger = models.ForeignKey(User)
    StationCode = models.ForeignKey(Stationdata)
    Subject = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    detail = models.TextField()
    Time = models.DateTimeField('Occurence')
    Place = models.CharField(max_length=200)

    def __str__(self):              # __unicode__ on Python 2
        return self.Subject

class Fir(models.Model):
    lodger = models.ForeignKey(User)
    StationCode = models.ForeignKey(Stationdata)
    Subject = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    detail = models.TextField()
    Suspect = models.CharField(max_length=500)
    Time = models.DateTimeField('Occurence')
    Place = models.CharField(max_length=200)
    Witness = models.CharField(max_length=500)
    Loss = models.CharField(max_length=200)

    def __str__(self):              # __unicode__ on Python 2
        return self.Subject
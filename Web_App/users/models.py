from django.db import models


class Fir(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    detail = models.TextField()


class General_Diary(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    details = models.TextField()
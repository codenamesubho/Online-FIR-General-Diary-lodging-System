from django.db.models.signals import post_save
from django.dispatch import receiver
from Web_App.models import Fir,General_Diary


@receiver(pre_save, sender=Fir)
def Fir_handler(sender, **kwargs):
	print "Signal triggered"


@receiver(pre_save, sender=General_Diary)
def Fir_handler(sender, **kwargs):
	print "Signal triggered"    
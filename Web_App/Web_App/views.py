from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Web_App.models import Fir
from police.models import Stationdata
from users.views import is_user
from django.utils import timezone


@login_required(login_url='/')
@is_user
def register_fir(request):
    title = request.POST['subject']
    suspect = request.POST['suspect']
    occurence = request.POST['occurence']
    location = request.POST['location']
    witness = request.POST['witness']
    loss = request.POST['loss']
    detail = request.POST['details']
    User = request.user
    StationCode = Stationdata.objects.get(StationCode="00012321")
    try:
        b = Fir( lodger=User, StationCode=StationCode, Subject=title, pub_date=timezone.now(),
         detail=detail, Suspect=suspect, Time=timezone.now(),Place=location, Witness=witness, Loss=loss)
        b.save()
    except Exception as e:
        print e
    return redirect('lodge_new')

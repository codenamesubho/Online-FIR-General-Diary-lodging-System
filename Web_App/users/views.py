from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Web_App.models import Fir,General_Diary
from collections import OrderedDict
#from operator import itemgetter
#from django.utils import timezone
from functools import wraps
from django.http import HttpResponse

def is_user(func):
    @wraps(func)
    def wrapper(request,*args,**kwargs):
        if 'is_user' not in request.session.keys():
            return HttpResponse("Not Authorized")
        return func(request,*args,**kwargs)
    return wrapper

def index(request):
	return render(request,'users/index.html')

@login_required(login_url='/')
@is_user
def dashboard(request):
    try:
        fir = Fir.objects.filter(lodger=request.user).order_by('-pub_date')[:4]
        generaldiary = General_Diary.objects.filter(lodger=request.user).order_by('-pub_date')[:4]
        lastfir = {data.pub_date:data for data in generaldiary}
        lastfir.update({data.pub_date:data for data in fir})
        lastfir = OrderedDict(sorted(lastfir.iteritems(),reverse=True)[:4])
        #print lastfir,dir(lastfir)
        return render(request,'users/dashboard.html',{ 'active' : 'dashboard' , 'report' : lastfir })
    except Exception as e:
        return HttpResponse(e)

@login_required(login_url='/')
@is_user
def lodge(request):
    return render(request,'users/new.html',{ 'active' : 'new' })


def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if (user.is_active and hasattr(user,'userdata')) or user.is_superuser :
            login(request, user)
            request.session['is_user'] = True
            return redirect('lodge_new')
        else:
            return HttpResponse("Not Authorized")
    else:
		return redirect('home')


@login_required(login_url='/')
def logout_user(request):
    logout(request)
    return redirect('home')


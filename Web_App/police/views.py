from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from Web_App.models import Fir,general_diary
from django.contrib.auth.models import User
from functools import wraps
from django.http import HttpResponse
from django.utils.html import strip_tags

# Create your views here.

"""
def police_login_required(login_url):
    def innerfunc(f):    
        @wraps(f)
        def wrap(request, *args, **kwargs):
            #this check the session if userid key exist, if not it will redirect to login page
            if '_auth_user_id' not in request.session.keys() or 'is_police' not in request.session.keys():
                    return redirect(login_url)
            return f(request, *args, **kwargs)
        return wrap
    return innerfunc
"""

def verify_police(func):
    @wraps(func)
    def wrapper(request,*args,**kwargs):
        if 'is_police' not in request.session.keys():
            return HttpResponse("Not Authorized")
        return func(request,*args,**kwargs)
    return wrapper


def index(request):
	return render(request,'police/index.html')

@login_required(login_url='/police/login')
@verify_police
def dashboard(request):
    try:
        stationcode = User.objects.get(pk=request.session['_auth_user_id']).stationdata.StationCode
        lastfir = Fir.objects.filter(StationCode__StationCode=stationcode).order_by('-pub_date')[:5]
        return render(request,'police/dashboard.html',{'Fir' : lastfir})
    except Exception as e:
        print e
        return HttpResponse(e)

def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if (user.is_active and hasattr(user,'stationdata')) or user.is_superuser:
            login(request, user)
            request.session['is_police'] = True
            print request.session.keys()
            return redirect('police_dashboard')
        else:
            return HttpResponse("Not Authorized")
    else:
		return redirect('police_login')


@login_required(login_url='/police/login')
def logout_user(request):
    logout(request)
    return redirect('police_login')



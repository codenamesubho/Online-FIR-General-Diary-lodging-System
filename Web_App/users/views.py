from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from Web_App.models import Fir
from django.utils import timezone
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
	return render(request,'users/dashboard.html',{ 'active' : 'dashboard' })

@login_required(login_url='/')
@is_user
def lodge(request):
    return render(request,'users/new.html',{ 'active' : 'new' })

@login_required(login_url='/')
@is_user
def register_fir(request):
    title = request.POST['title']
    detail = request.POST['detail']
    try:
        b = Fir(title = title, detail = detail, pub_date=timezone.now())
        b.save()
    except Exception as e:
        print e
    return redirect('dashboard')


def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            request.session['is_user'] = True
            return redirect('lodge_new')
    else:
		return redirect('home')


@login_required(login_url='/')
def logout_user(request):
    logout(request)
    return redirect('home')
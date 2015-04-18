from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from Web_App.models import Fir
from django.utils import timezone

def index(request):
	return render(request,'users/index.html')

@login_required(login_url='/')
def dashboard(request):
	return render(request,'users/dashboard.html',{ 'active' : 'dashboard' })

@login_required(login_url='/')
def lodge(request):
    return render(request,'users/new.html',{ 'active' : 'new' })

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
            return redirect('dashboard')
    else:
		return redirect('home')

def logout_user(request):
    logout(request)
    return redirect('home')
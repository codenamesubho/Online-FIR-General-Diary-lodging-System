from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from Web_App.models import Fir
# Create your views here.

def index(request):
	return render(request,'police/index.html')

@login_required(login_url='/police/login')
def dashboard(request):
    lastfir = Fir.objects.order_by('-pub_date')[:5]
    print lastfir
    return render(request,'police/dashboard.html',{'Fir' : lastfir})

def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('police_dashboard')
    else:
		return redirect('police_login')

def logout_user(request):
    logout(request)
    return redirect('police_login')
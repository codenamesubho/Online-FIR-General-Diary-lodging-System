from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
	return render(request,'index.html')

@login_required(login_url='/')
def dashboard(request):
	return render(request,'userdash.html')

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

def logout_view(request):
    logout(request)
    return redirect('home')
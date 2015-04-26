from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from Web_App.models import Fir
from functools import wraps
# Create your views here.

def police_login_required(login_url):
    def innerfunc(f):    
        @wraps(f)
        def wrap(request, *args, **kwargs):
            #this check the session if userid key exist, if not it will redirect to login page
            print request.session.keys(),request.session.values()
            if '_auth_user_id' not in request.session.keys() or 'is_police' not in request.session.keys():
                    return redirect(login_url)
            return f(request, *args, **kwargs)
        return wrap
    return innerfunc


def index(request):
	return render(request,'police/index.html')

@police_login_required(login_url='/police/login')
def dashboard(request):
    lastfir = Fir.objects.order_by('-pub_date')[:5]
    return render(request,'police/dashboard.html',{'Fir' : lastfir})

def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            request.session['is_police'] = True
            print request.session.keys()
            return redirect('police_dashboard')
    else:
		return redirect('police_login')

def logout_user(request):
    logout(request)
    return redirect('police_login')



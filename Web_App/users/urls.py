from django.conf.urls import patterns, url
from police import views

urlpatterns = patterns('',
	url(r'^authenticate/', 'users.views.login_user', name='authenticate'),
    url(r'^dashboard/new/$', 'users.views.lodge', name='lodge_new'),
    url(r'^dashboard/$', 'users.views.dashboard', name='dashboard'),
    url(r'^settings/$', 'users.views.dashboard', name='settings'),
    url(r'^logout', 'users.views.logout_user', name='logout'),
    
    
    )
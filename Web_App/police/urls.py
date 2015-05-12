from django.conf.urls import patterns, url
from police import views

urlpatterns = patterns('',
        url(r'^login', 'police.views.index', name='police_login'),
		url(r'^dashboard', 'police.views.dashboard', name='police_dashboard'),
		url(r'^authenticate', 'police.views.login_user', name='police_auth'),
		url(r'^logout', 'police.views.logout_user', name='police_logout'),
		url(r'^getoption','police.views.dashboard',name='getoption')
    )


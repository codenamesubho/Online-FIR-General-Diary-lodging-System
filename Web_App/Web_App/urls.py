from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Web_App.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'Web_App.views.index', name='home'),
    url(r'^authenticate/', 'Web_App.views.login_user', name='authenticate'),
    url(r'^user/dashboard/', 'Web_App.views.dashboard', name='dashboard'),
    url(r'^logout', 'Web_App.views.logout_user', name='logout'),
    url(r'^register/', 'Web_App.views.register_fir', name='register'),
    url(r'^police/login', 'police.views.index', name='police_login'),
    url(r'^police/dashboard', 'police.views.dashboard', name='police_dashboard'),
    url(r'^police/authenticate', 'police.views.login_user', name='police_auth'),
    url(r'^police/logout', 'police.views.logout_user', name='police_logout'),
    
    url(r'^admin/', include(admin.site.urls)),


)

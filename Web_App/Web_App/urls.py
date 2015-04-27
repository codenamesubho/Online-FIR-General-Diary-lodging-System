from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Web_App.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'users.views.index', name='home'),
    url(r'^user/' , include('users.urls')),
    url(r'^police/' , include('police.urls')),
    url(r'^register/', 'Web_App.views.register_fir', name='register'),
    url(r'^admin/', include(admin.site.urls)),


)

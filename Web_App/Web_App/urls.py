from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Web_App.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'users.views.index', name='home'),
    url(r'^new/$', 'users.views.lodge', name='lodge_new'),
    url(r'^resend/', 'Web_App.views.resend', name='resend'),
    url(r'^verify/','Web_App.views.verify_otp', name="verifyOtp"),
    url(r'^success/','Web_App.views.success', name="pdf"),
    url(r'^dashboard/$', 'users.views.dashboard', name='dashboard'),
    url(r'^settings/$', 'users.views.dashboard', name='settings'),
    url(r'^police/' , include('police.urls')),
    url(r'^register/$', 'Web_App.views.register_report', name='register'),
    url(r'^admin/', include(admin.site.urls)),


)

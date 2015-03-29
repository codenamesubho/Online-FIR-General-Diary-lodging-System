from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Web_App.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'Web_App.views.index', name='home'),
    url(r'^authenticate/', 'Web_App.views.login_user', name='authenticate'),
    url(r'^user/dashboard/', 'Web_App.views.dashboard', name='dashboard'),
    url(r'^logout', 'Web_App.views.logout_view', name='logout'),
    url(r'^admin/', include(admin.site.urls)),
)

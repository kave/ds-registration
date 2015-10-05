from django.conf.urls import patterns, include, url
from core.views import home, RegisterView, success

urlpatterns = patterns('',
                       url(r'^$', home, name='home'),
                       url(r'^register/$', RegisterView.as_view(), name='register'),
                       url(r'^success/$', success, name='success'),
                       )

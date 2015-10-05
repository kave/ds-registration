from django.conf.urls import patterns, include, url
from core.views import home

urlpatterns = patterns('',
                       url(r'^$', home, name='cards'),
                       )

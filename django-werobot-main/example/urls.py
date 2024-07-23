# example/urls.py
from django.conf.urls import patterns, include, url
from werobot.contrib.django import make_view
from example.views import index
from robot import myrobot

urlpatterns = patterns('',
    url(r'^robot/', make_view(myrobot)),
)
from django.conf.urls import url
from django.http import HttpResponse

from . import views

urlpatterns = [
    url(r'^$', views.test, name='index'),
    url(r'^login/$', views.test, name='login'),
    url(r'^signup/$', views.test, name='signup'),
    url(r'^question/(?P<id>[0-9]+)/$', views.test, name='question'),
    url(r'^ask/$', views.test, name='ask'),
    url(r'^popular/$', views.test, name='popular'),
    url(r'^new/$', views.test, name='new'),
]
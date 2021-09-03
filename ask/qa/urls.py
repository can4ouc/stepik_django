from django.conf.urls import url
from django.http import HttpResponse

from . import views
from .views import question, popular, index, ask

urlpatterns = [
    url(r'^$', index, name='index'),
    # url(r'^login/$', views.test, name='login'),
    # url(r'^signup/$', views.test, name='signup'),
    url(r'^question/(?P<pk>\d+)/', question, name='question'),
    url(r'^ask/$', ask, name='ask'),
    url(r'^popular/$', popular, name='popular'),
    # url(r'^new/$', views.test, name='new'),
    #url(r'^(?P<num>\d+)/$', question),
]
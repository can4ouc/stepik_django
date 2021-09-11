from django.conf.urls import url
from django.http import HttpResponse

from . import views
from .views import question, popular, index, ask, user_login, user_logout

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^login/$', user_login, name='login'),
    url(r'^signup/$', user_logout, name='signup'),
    url(r'^question/(?P<num>\d+)/', question, name='question'),
    url(r'^ask/$', ask, name='ask'),
    url(r'^popular/$', popular, name='popular'),
    url(r'^logout/', user_logout, name='logout'),
    # url(r'^new/$', views.test, name='new'),
    #url(r'^(?P<num>\d+)/$', question),
]
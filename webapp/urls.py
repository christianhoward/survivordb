from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^player/(?P<pk>\d+)/$', views.player, name='player'),
    url(r'^season/(?P<pk>\d+)/$', views.season, name='season'),
    url(r'^seasons/$', views.seasons, name='seasons'),
]
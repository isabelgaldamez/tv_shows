from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^shows$', views.all_shows),
    url(r'^shows/new$', views.show_new),
    url(r'^create$', views.create),
    url(r'^shows/(?P<show_id>\d+)$', views.display),
    url(r'^shows/(?P<show_id>\d+)/edit$', views.edit),
    url(r'^shows/(?P<show_id>\d+)/update$', views.update),
    url(r'^shows/(?P<show_id>\d+)/destroy$', views.destroy),
]
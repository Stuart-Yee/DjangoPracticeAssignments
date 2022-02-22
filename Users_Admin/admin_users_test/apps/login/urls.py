from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^display/$', views.display),
    url(r'^accounts/profile/$', views.profile),
    url(r'^$', views.index),
    url(r'^logout/$', views.logout_user),
    url(r'^dashboard/$', views.secret_stuff)
]

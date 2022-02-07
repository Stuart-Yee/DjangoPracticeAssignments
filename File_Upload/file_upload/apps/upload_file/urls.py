from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^upload$', views.upload),
    url(r'^clear$', views.clear)
]

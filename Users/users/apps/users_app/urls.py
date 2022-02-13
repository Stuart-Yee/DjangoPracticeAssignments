from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^users$', views.index),
    url(r'^new_user$', views.new_user),
    url(r"^$", views.root)
]

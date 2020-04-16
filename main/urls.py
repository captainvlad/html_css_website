from django.conf.urls import url
from . import views

urlpatterns = [
    url('main', views.respond_1, name = "index"),
    url('home_3', views.respond_3, name = "index"),
    url('home_2', views.respond_2, name = "index"),
    url('home_4', views.respond_4, name = "index"),
    url('home_5', views.respond_5, name = "index"),
    url('home_6', views.respond_7, name = "index"),
    url('home_7', views.respond_6, name = "index"),
    url('home_9', views.respond_8, name = "index"),
    url('home_10', views.respond_9, name = "index"),
    url('home_11', views.respond_10, name = "index"),
    url('home_12', views.respond_11, name = "index"),
]
from django.urls import path

from . import views

urlpatterns = [ 
    path("list/", views.view, name="index"),
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("view/", views.view, name="view"),
]


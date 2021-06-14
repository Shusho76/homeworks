from django.urls import path
from . import views

urlpatterns = [
    path('', views.greeting),
    path("int/", views.introduction),
    path("data/", views.data_time),
    path("dict/", views.dictionary_)


]


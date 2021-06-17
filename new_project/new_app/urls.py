from django.urls import path
from . import views


urlpatterns = [
    path("", views.home),
    path("greeting/", views.greeting),
    path("greeting1/", views.greeting1),
    path("hello-html/", views.hello_html),
    path("home/", views.hello),
    path("json/", views.json_file),
    path("place/", views.massege)


    ]

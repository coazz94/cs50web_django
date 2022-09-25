from django.urls import path 

from . import views

app_name = "tasks"     #indetifzierung von genau dieser app
urlpatterns = [
    path("", views.index , name="index"),
    path("add", views.add , name="add")
]


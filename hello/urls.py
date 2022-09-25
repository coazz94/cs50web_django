from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("aleks", views.aleks, name="aleks"),
    path("<str:name>", views.greet, name="greet"),
]



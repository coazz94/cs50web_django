from curses.ascii import HT
from django.http import HttpResponse
from django.shortcuts import render

#Create your views here.
#request the user made
def index(request): 
    return render(request, "hello/index.html")

def aleks(request):
    return HttpResponse("Hello, Aleks")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })


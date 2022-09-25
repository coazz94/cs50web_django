from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#request the user made
def index(request): 
    return HTTPResponse("Hello, world!")

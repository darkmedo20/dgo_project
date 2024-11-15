from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Welcome to my first django app!")

def bio(request):
    return HttpResponse('<h1 style="color: blue;"> Ahmed Almostafa, Software Engineer @micro1</h1>')
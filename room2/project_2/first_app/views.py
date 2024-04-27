from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home (request):
    return HttpResponse("This is a first_app Home page")
def courses (request):
    return HttpResponse("This is a courses page")
def about (request):
    return HttpResponse("This is app page.This is a about page")
from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("HELLO WORLD")

def displayname(request):
    return HttpResponse("Name")
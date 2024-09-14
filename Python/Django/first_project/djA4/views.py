from django.shortcuts import render, HttpResponse
from datetime import datetime
# Create your views here.

def index(request):
    info = {
        "name":"Abshir",
        "food": "Tikka Masala",
        "vacation": "Tulum"
    }
    return render(request, "index.html", context = info )

def numbers(request):
    return render(request, "nums.html", context = {"nums": [1,2,3,4,5,6,7,8,9,10]})


def printdata(request):
    info = {
        "name" : request.POST['name'],
        "email" : request.POST['email'],
        "food" : request.POST['food']
    }
    
    return render(request, "info.html", context = info )
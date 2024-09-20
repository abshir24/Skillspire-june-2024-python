from django.shortcuts import render, HttpResponse
from datetime import datetime
from .models import User
# Create your views here.

def index(request):
    return render(request, "index.html")

def printdata(request):
    user = User.objects.create(name = request.POST['name'], email = request.POST['email'])

    return render(request, 'name.html', context = {'user': user})
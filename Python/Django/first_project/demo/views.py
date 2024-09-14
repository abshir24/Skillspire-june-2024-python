from django.shortcuts import render, HttpResponse
from datetime import datetime
# Create your views here.

def index(request):
    return render(request, "index.html")

def printdata(request):
    name = request.POST['name'] #request.form['name'] <---- Flask version

    return render(request, 'name.html', context = {'name': name})
from django.shortcuts import render, HttpResponse
from datetime import datetime
# Create your views here.

def index(request):
    return render(request, "index.html")


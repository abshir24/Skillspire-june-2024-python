from django.shortcuts import render, HttpResponse
from datetime import datetime
# Create your views here.

def index(request):
    return render(request, "index.html", context = {"arr_nums": [1,2,3,4,5,6,7,9,10]})


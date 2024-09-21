from django.shortcuts import render, HttpResponse,redirect

from .models import User
# Create your views here.

def index(request):
    all_users = User.objects.all()
    return render(request, "index.html", context={"users": all_users})

def adduser(request):
    name = request.POST['name']
    height = request.POST['height']
    weight = request.POST['weight']
    dietary_preference = request.POST['dietary_preference']

    user = User.objects.create(name = name, height = height, weight = weight, dietary_preference = dietary_preference)

    return redirect('/')


def displayuser(request, user_id):
   user = User.objects.get(id = user_id) 

   return render(request,"user.html", context = { "user": user })
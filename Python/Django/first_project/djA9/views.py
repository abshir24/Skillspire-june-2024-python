from django.shortcuts import render, HttpResponse,redirect
from .models import User
# Create your views here.

def index(request):
    all_users = User.objects.all()
    return render(request, "index.html", context = { "users": all_users })

def adduserform(request):
    return render(request, "adduser.html")
    
def adduser(request):
    User.objects.create(name = request.POST['name'], email = request.POST['email'])

    return redirect('/')

def showuser(request,user_id):
    user = User.objects.get(id=user_id)

    return render(request, "showuser.html", context={"user": user})

def edituserform(request, user_id):
    return render(request, 'edituserform.html', context={"user_id": user_id})

def edituser(request, user_id):
    user = User.objects.get(id=user_id)

    user.name = request.POST['name']
    user.email = request.POST['email']

    user.save()

    return redirect('/')
    
def deleteuser(request,user_id):
    user = User.objects.get(id=user_id)

    user.delete()

    return redirect('/')

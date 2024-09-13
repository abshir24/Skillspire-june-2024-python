from django.shortcuts import render, HttpResponse
from datetime import datetime
# Create your views here.

def index(request):
    name = "Abshir"
    return render(request, "index.html", context = {"name":name})

def displayinfo(request):
    name = "Abshir"
    food = "Indian food"
    movie = "Black Panther 1!"
    music = "Afro-beats"

    return HttpResponse(f"Name: {name} Favorite Food: {food} Movie: {movie} Music Genre: {music}")

def displaytime(request):
    current_time = datetime.now()

    return render(request, "time.html",context = {"current_time": current_time} )


def displayname(request, name):
    return render(request, "name.html", context = {"name": name} )
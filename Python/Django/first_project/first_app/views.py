from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    name = "Abshir"
    return render(request, "index.html", context = { "name": name })


def displayinfo(request):
    name = "Abshir"
    food = "Indian food"
    movie = "Black Panther 1!"
    music = "Afro-beats"

    return HttpResponse(f"Name: {name} Favorite Food: {food} Movie: {movie} Music Genre: {music}")
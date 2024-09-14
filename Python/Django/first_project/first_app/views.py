from django.shortcuts import render, HttpResponse
from datetime import datetime
# Create your views here.

def index(request):
    return render(request, "index.html")

# --------------------------------------------------------
def displayinfo(request):
    # CODE FOR ASSIGNMENT 1
    name = "Abshir"
    food = "Indian food"
    movie = "Black Panther 1!"
    music = "Afro-beats"

    return HttpResponse(f"Name: {name} Favorite Food: {food} Movie: {movie} Music Genre: {music}")

# --------------------------------------------------------

# --------------------------------------------------------

def displaytime(request):

    # CODE FOR ASSIGNMENT 2
    current_time = datetime.now()

    return render(request, "time.html",context = {"current_time": current_time} )


# --------------------------------------------------------

# CODE FOR ASSIGNMENT 3
def displayname(request, name):
   return render(request, "name.html" , context = { "name": name } ) 

def displayfood(request, food):
   return render(request, "food.html" , context = { "food": food } ) 

def displayvacation(request, vacation):
   return render(request, "vacation.html" , context = { "vacation": vacation } ) 
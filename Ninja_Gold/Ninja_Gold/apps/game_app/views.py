from django.shortcuts import render, HttpResponse
from random import randint

# Create your views here.
def index(request):
    try:
        gold = request.session["gold"]
    except:
        request.session["gold"] = 0
        gold = 0

    data = {"gold": gold}

    return render(request, "index.html", data)
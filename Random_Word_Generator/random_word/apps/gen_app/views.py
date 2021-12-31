from django.shortcuts import render, redirect
from random import randint

# Create your views here.
def index(request):
    return render(request, "index.html")

def word(request):
    try:
        request.session["visits"] += 1
    except:
        request.session["visits"] = 1
    new_word =""
    for i in range(14):
        new_word += chr(randint(97,122))

    word = {"word": new_word}
    return render(request, "random_word.html", word)

def reset(request):
    request.session["visits"] = 0
    return redirect("/random_word")
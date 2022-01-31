from django.shortcuts import render, redirect
from . import models

# Create your views here.

def index(request):
    context = {"users": models.User.objects.all()}

    return render(request, "index.html", context=context)

def new_user(request):

    if request.method == "POST":
        models.User.objects.create(
            first_name=request.POST["first_name"],
            last_name=request.POST["last_name"],
            email_address=request.POST["email"],
            age=int(request.POST["age"]),
        )


    return redirect("/users")

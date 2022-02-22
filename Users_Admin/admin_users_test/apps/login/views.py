from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def display(request):
    if 'first_name' in dir(request.user):
        context = {"logged_name": request.user.first_name + " " + request.user.last_name}
    else:
        context = {"logged_name": "Guest"}
    return render(request, "display.html", context)

def profile(request):
    return redirect("/display")

def index(reqquest):
    return redirect("/dashboard")

def logout_user(request):
    logout(request)
    return redirect("/display")

@login_required(redirect_field_name='display')
def secret_stuff(request):
    return render(request, "private.html")
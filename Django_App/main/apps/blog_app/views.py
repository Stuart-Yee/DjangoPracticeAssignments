from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response = "Testing"
    return HttpResponse(response)

def new(request):
    response = "Placeholder for new blog"
    return HttpResponse(response)

def create(request):
    return redirect("/")

def show(request, number):
    response = f"Placeholder to display blog {number}"
    return HttpResponse(response)

def edit(request, number):
    response = f"placeholder to edit blog {number}"
    return HttpResponse(response)

def delete(request, number):
    return redirect("/")
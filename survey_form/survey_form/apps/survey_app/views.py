from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    languages = [
        "C++",
        "Java",
        "Python"
    ]

    locations = [
        "San Jose",
        "Seattle",
        "Online"
    ]

    data = {"languages": languages, "locations": locations}

    return render(request, "index.html", data)

def submit(request):
    for thing in request.POST:
        request.session[thing] = request.POST[thing]
    try:
        request.session["submissions"] += 1
    except:
        request.session["submissions"] = 1
    return redirect("/result")

def result(request):
    return render(request, "result.html")

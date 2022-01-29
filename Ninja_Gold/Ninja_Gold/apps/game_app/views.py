import inspect

from django.shortcuts import render, HttpResponse, redirect
from random import randint
from time import strftime, localtime
from functools import wraps

# decorator to run method only if request.method == "POST"
# Otherwise redirects to "/"
def post_only(f):
    @wraps(f)
    def inner(*args, **kwargs):
        for arg in args:
            try:
                method = arg.method
                break
            except:
                continue
        if method == "POST":
            return f(*args, **kwargs)
        else:
            return redirect("/")
    return inner



# Create your views here.


def index(request):
    now = strftime("%Y/%m/%d %I:%M %p", localtime())

    try:
        gold = request.session["gold"]
    except:
        request.session["gold"] = 0
        gold = 0

    try:
        logs = request.session["logs"]
    except:
        request.session["logs"] = []
        logs = []
        print("Had to create new session")

    data = {
        "gold": gold,
        "logs": logs,
    }

    return render(request, "index.html", data)

@post_only # execute only from the button, not from a GET
def farm(request):
    # farms produce 10 - 20 gold
    now = strftime("%Y/%m/%d %I:%M %p", localtime())
    gold = request.session["gold"]
    found_gold = randint(10, 20)
    gold += found_gold
    request.session["gold"] = gold

    logs = request.session["logs"]
    log = {"activity": f"Found {found_gold} GOLD at the farm! ({now})",
           "change": "gain"}
    logs.append(log)
    request.session["logs"] = logs
    return redirect("/")

@post_only
def cave(request):
    # caves product 5-10 gold
    now = strftime("%Y/%m/%d %I:%M %p", localtime())
    gold = request.session["gold"]
    found_gold = randint(5, 10)
    gold += found_gold
    request.session["gold"] = gold

    logs = request.session["logs"]
    log = {"activity": f"Found {found_gold} GOLD in the cave! ({now})",
           "change": "gain"}
    logs.append(log)
    request.session["logs"] = logs
    return redirect("/")

@post_only
def house(request):
    # houses produce 2-5 gold
    now = strftime("%Y/%m/%d %I:%M %p", localtime())
    gold = request.session["gold"]
    found_gold = randint(2, 5)
    gold += found_gold
    request.session["gold"] = gold

    logs = request.session["logs"]
    log = {"activity": f"Found {found_gold} GOLD at the house! ({now})",
           "change": "gain"}
    logs.append(log)
    request.session["logs"] = logs
    return redirect("/")

@post_only
def casino(request):
    # you can win or lose 0-50
    now = strftime("%Y/%m/%d %I:%M %p", localtime())
    gold = request.session["gold"]
    found_gold = randint(-50, 50)
    gold += found_gold
    request.session["gold"] = gold

    logs = request.session["logs"]
    if found_gold < 0:
        log = {"activity": f"LOST {found_gold*-1} GOLD at the casino... ouch! ({now})",
               "change": "loss"}
    else:
        log = {"activity": f"WON {found_gold} GOLD at the casino! ({now})",
               "change": "gain"}

    logs.append(log)
    request.session["logs"] = logs
    return redirect("/")

@post_only
def reset(request):
    request.session["logs"] = []
    request.session["gold"] = 0
    return redirect("/")

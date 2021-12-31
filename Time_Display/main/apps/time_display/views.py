from django.shortcuts import render, HttpResponse
from time import gmtime, strftime, localtime

# Create your views here.
def index(request):
    data = {
        "gmt_time": strftime("%Y-%m-%d %I:%M %p", gmtime()),
        "local_time": strftime("%Y-%m-%d %I:%M %p", localtime())
    }
    return render(request, "index.html", data)
from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.
def display(request):
    print(request.user.first_name)
    print(request.user.get_full_name())
    print(request.user)
    print(dir(request.user))
    return render(request, "display.html")

def logout_view(request):
    logout(request)
    return redirect("/display")
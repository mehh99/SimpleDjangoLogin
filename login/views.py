from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from login.forms import LoginForm, RegistrationForm

def index(request):
    return render(request, "index.html", {"form": LoginForm()})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=request.POST["username"], password=request.POST["password"]
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, "enter.html")
        else:
            return render(request, "login.html", {"form": form})
    else:
        return render(request, "login.html", {"form": LoginForm()})

    return redirect("enter.html")


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=request.POST["username"],
                email=request.POST["email"],
                password=request.POST["password"],
            )
            return redirect("auth:login")
        else:
            return render(request, "register.html", {"form": form})
    else:
        return render(request, "register.html", {"form": RegistrationForm()})


def logout_view(request):
    logout(request)
    return render(request, "login.html", {"form": LoginForm()})

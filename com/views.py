from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User, auth


# Create your views here.


def index(request):
    return render(request, "index.html")


def register(request):
    if request.method == "POST":
        username = username.POST["username"]
        email = email.POST["email"]
        password = password.POST["password"]
        confirm_password = confirm_password.POST["confirm_password"]

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email taken")
                return redirect("register")
            else:
                user = User.objects.create_user(
                    username=username, password=password, email=email
                )
                user.save()
                print("user created")
                return redirect("home")

        else:
            messages.info(request, "password not matching.....")
            return redirect("register")

        return redirect("index.html")
    else:
        return render(request, "register.html")

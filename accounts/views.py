from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, auth
from django.contrib import messages


# def login(request):
#    if request.method == "POST":
#        username = request.POST["username"]
#        password = request.POST["password"]

#        user = auth.authenticate(username=username, password=password)

#        if user is not None:
#            auth.login(request, user)
#            return redirect("index")
#        else:
#           messages.info(request, "invalid credentials")
#          return redirect("login")

# else:
#    return render(request, "login.html")


# def register(request):
#    if request.method == "POST":
#        firstname = request.POST["firstname"]
#        lastname = request.POST["lastname"]
#       username = request.POST["username"]
#        email = request.POST["email"]
#        password = request.POST["password"]
#        confirm_password = request.POST["confirm_password"]
#
#        if password == confirm_password:
#            if User.objects.filter(username=username).exists():
#                messages.info(request, "username taken")
#               return redirect("register")
#           if User.objects.filter(email=email).exists():
#                messages.info(request, "email taken")
#                return redirect("register")

#           user = User(
#                username=username,
#                email=email,
#            )
#            user.set_password(password)
#           user.save()
#            print("user created")
#            return redirect("index")

#        else:
#            messages.info(request, "password not matching.....")
#            return redirect("register")

#    else:
#        return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect("index")

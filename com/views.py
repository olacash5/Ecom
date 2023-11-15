from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User, auth


# Create your views here.


def index(request):
    # if request.method == "POST":
    return render(request, "index.html")

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User, auth


# Create your views here.


def index(request):
    return render(request, "index.html")


def cart(request):
    return render(request, "cart.html")


def contact(request):
    return render(request, "contact.html")


def customer_profile(request):
    return render(request, "customer_profile.html")


def my_wallet(request):
    return render(request, "my_wallet.html")


def my_reward(request):
    return render(request, "my_reward.html")


def my_order(request):
    return render(request, "my_order.html")


def payment_method(request):
    return render(request, "payment_method.html")


def boolean(request):
    return render(request, "boolean.html")

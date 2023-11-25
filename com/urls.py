from django.urls import path
from . import views


urlpatterns = [
    path("index", views.index, name="index"),
    path("cart", views.cart, name="cart"),
    path("contact", views.contact, name="contact"),
]

from django.urls import path
from . import views


urlpatterns = [
    path("index", views.index, name="index"),
    path("cart", views.cart, name="cart"),
    path("contact", views.contact, name="contact"),
    path("customer_profile", views.customer_profile, name="customer_profile"),
    path(
        "personal_information", views.personal_information, name="personal_information"
    ),
]

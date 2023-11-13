from django.urls import path
from . import views


urlpatterns = [
    path("index", views.index, name="index.html"),
    path("register", views.register, name="register.html"),
]

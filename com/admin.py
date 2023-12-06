from django.contrib import admin
from .models import Profile, Seller, Buyer

# Register your models here.

admin.site.register([Profile, Seller, Buyer])

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    bio = models.TextField()
    phone = models.TextField()
    username = models.TextField()

    is_seller = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Seller(models.Model):
    profile = models.OneToOneField(
        Profile, related_name="seller", on_delete=models.CASCADE
    )
    Business_name = models.TextField()

    def __str__(self):
        return f"seller {self.profile.user.username}"


class Buyer(models.Model):
    profile = models.OneToOneField(
        Profile, related_name="buyer", on_delete=models.CASCADE
    )
    username = models.TextField()

    def __str__(self):
        return f"buyer {self.profile.user.username}"


@receiver(post_save, sender=User)
def NotifyProfile(sender, created, instance, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance, bio="Hello")

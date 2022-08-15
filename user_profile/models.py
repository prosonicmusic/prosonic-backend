from operator import mod
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=f"uploads/images/avatar", max_length=254)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    provice = models.CharField(max_length=100, blank=True, null=True)
    verified = models.BooleanField(default=False)
    otp = models.IntegerField(blank=True, null=True)
    otp_expire_time = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        return self.user.username

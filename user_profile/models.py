from operator import mod
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.URLField(max_length=300)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    provice = models.CharField(max_length=100, blank=True, null=True)
    verified = models.BooleanField(default=False)
    otp = models.IntegerField(blank=True, null=True)
    otp_expire_time = models.DateTimeField(blank=True, null=True)

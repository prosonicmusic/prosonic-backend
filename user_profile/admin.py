from django.contrib import admin

from .models import *


@admin.register(UserProfile)
class CustomUserProfile(admin.ModelAdmin):
    list_display = ("user_id", "verified")

from itertools import product
from rest_framework import serializers
from .models import UserProfile
from prosonic_backend_core import settings
from django.contrib.auth.models import User


class BaseUserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = (
            "password",
            "is_superuser",
            "last_login",
            "is_staff",
            "is_active",
            "date_joined",
            "groups",
            "user_permissions",
        )


class UserInfoSerializer(serializers.ModelSerializer):
    user = BaseUserInfoSerializer()

    class Meta:
        model = UserProfile
        exclude = ("id",)
        depth = 1


class UserRegisterationSerializer(serializers.ModelSerializer):
    pass

import email
from enum import unique
from itertools import product
from .models import UserProfile
from prosonic_backend_core import settings
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model  # If used custom user model
from rest_framework.validators import UniqueValidator

UserModel = get_user_model()


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

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    def create(self, validated_data):

        user = UserModel.objects.create_user(
            email=validated_data["email"],
            username=validated_data["email"],
        )
        user.set_password(validated_data["password"])
        user.save()

        UserProfile.objects.create(user=user)

        return user

    class Meta:
        model = UserModel
        fields = ("id", "password", "email")

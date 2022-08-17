import email
from enum import unique
from itertools import product
from wsgiref.validate import validator
from .models import UserProfile
from prosonic_backend_core import settings
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model  # If used custom user model
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.shortcuts import get_object_or_404

UserModel = get_user_model()


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        user_profile = get_object_or_404(UserProfile, id=self.user.id)
        data.update({"verified": user_profile.verified})
        data.update({"username": self.user.username})
        data.update({"id": self.user.id})
        return data


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
    name = serializers.CharField(max_length=254, allow_blank=True, allow_null=True)
    password = serializers.CharField(validators=[validate_password])

    def create(self, validated_data):

        user = UserModel.objects.create_user(
            email=validated_data["email"],
            username=validated_data["email"],
            first_name=validated_data["name"],
        )
        user.set_password(validated_data["password"])
        user.save()

        UserProfile.objects.create(user=user)

        return user

    class Meta:
        model = UserModel
        fields = ("id", "first_name", "name", "password", "email")

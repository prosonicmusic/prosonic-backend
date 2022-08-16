import statistics
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from user_profile.serializers import UserInfoSerializer, UserRegisterationSerializer
from .models import UserProfile
from django.contrib.auth import get_user_model

UserModel = get_user_model()
# Create your views here.
class UserInfo(APIView):
    permission_classes = []

    def get(self, request):
        try:
            id = self.request.query_params.get("id")
            user = get_object_or_404(UserModel, pk=id)
            obj = UserProfile.objects.get(user=user)
            serialized_user = UserInfoSerializer(obj)
            return Response(serialized_user.data)
        except Exception as e:
            print(e)
            raise e


# Create your views here.
class Register(APIView):
    def post(self, request):
        try:
            user_id = 0
            serialized = UserRegisterationSerializer(data=request.data)
            if serialized.is_valid():
                user = serialized.create(serialized.data)
                user_id = user.id
            else:
                return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"user_id": user_id, "message": "User created!"})
        except Exception as e:
            print(e)
            raise e

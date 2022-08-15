from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from user_profile.serializers import UserInfoSerializer
from .models import UserProfile
from django.contrib.auth.models import User

# Create your views here.
class UserInfo(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            id = self.request.query_params.get("id")
            user = get_object_or_404(User, pk=id)
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
            return Response()
        except Exception as e:
            print(e)
            raise e

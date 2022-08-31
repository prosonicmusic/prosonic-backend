from datetime import datetime
import statistics
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from prosonic_backend_core.utils import GenerateResetCode, customResponse
from user_profile.serializers import UserInfoSerializer, UserRegisterationSerializer
from .models import UserProfile
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer, UserVerificationSerializer
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage

UserModel = get_user_model()


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    token_obtain_pair = TokenObtainPairView.as_view()


class UserInfo(APIView):
    permission_classes = []

    def get(self, request):
        try:
            id = self.request.query_params.get("id")
            user = get_object_or_404(UserModel, pk=id)
            obj = UserProfile.objects.get(user=user)
            serialized_user = UserInfoSerializer(obj)
            return customResponse(
                data=serialized_user.data,
                status=200,
                message="",
                success=1,
                http=status.HTTP_200_OK,
            )
        except Exception as e:
            print(e)
            raise e


class Register(APIView):
    def post(self, request):
        try:
            user_id = 0
            serialized = UserRegisterationSerializer(data=request.data)
            if serialized.is_valid():
                user = serialized.create(serialized.data)
                user_id = user.id
            else:
                return customResponse(
                    data=[],
                    status=400,
                    message=serialized._errors,
                    success=0,
                    http=status.HTTP_400_BAD_REQUEST,
                )
            return customResponse(
                data=user_id,
                message="User created!",
                status=200,
                success=1,
                http=status.HTTP_200_OK,
            )
        except Exception as e:
            print(e)
            raise e


class CheckVerification(APIView):
    permission_classes = []

    def get(self, requrest):
        try:
            user_id = self.request.query_params.get("user_id")
            user = get_object_or_404(UserModel, pk=user_id)
            user_profile = get_object_or_404(UserProfile, pk=user.id)

            return customResponse(
                success=1,
                data=user_profile.verified,
                message="",
                status=200,
                http=status.HTTP_200_OK,
            )
        except Exception as e:
            print(e)
            raise e


class SendVerification(APIView):
    permission_classes = []

    def post(self, request):
        try:
            code = GenerateResetCode(5)
            user_id = self.request.query_params.get("user_id")
            user = get_object_or_404(UserModel, pk=user_id)
            user_profile = get_object_or_404(UserProfile, pk=user.id)
            user_profile.otp = code
            user_profile.otp_expire_time = datetime.now()
            # todo : check for last otp time
            user_profile.save()

            send_email(email=user.email)
            return customResponse(
                success=1,
                data=[],
                message="Verification code sent",
                status=200,
                http=status.HTTP_200_OK,
            )
        except Exception as e:
            print(e)
            raise e


class VerifyUser(APIView):
    permission_classes = []

    def post(self, request):
        try:
            serialized = UserVerificationSerializer(data=request.data)
            if serialized.is_valid():
                user = get_object_or_404(UserModel, email=serialized.data["email"])
                user_profile = get_object_or_404(UserProfile, user=user)
                user_code = user_profile.otp
                # todo : check otp time
                if user_code == int(serialized.data["code"]):
                    user_profile.verified = True
                    user_profile.save()
                else:
                    return customResponse(
                        success=0,
                        message="Otp is wrong",
                        data=[],
                        status=400,
                        http=status.HTTP_400_BAD_REQUEST,
                    )

                return customResponse(
                    success=1,
                    message="User verified",
                    data=[],
                    status=200,
                    http=status.HTTP_200_OK,
                )
            else:
                return customResponse(
                    message=serialized._errors,
                    status=400,
                    data=[],
                    success=0,
                    http=status.HTTP_400_BAD_REQUEST,
                )
        except Exception as e:
            print(e)
            raise e


def send_email(email: str):
    email = EmailMessage(
        "Title",
        (
            "ConsultSerializer.name",
            "ConsultSerializer.email",
            "ConsultSerializer.phone",
        ),
        "prosonicweb@gmail.com",
        [email],
    )

    email.send()

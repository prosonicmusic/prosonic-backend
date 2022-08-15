from django.urls import path
from . import views

urlpatterns = [
    path("get", views.UserInfo.as_view(), name="get_user"),
    path("register", views.Register.as_view(), name="register_user"),
]

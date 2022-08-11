from django.urls import path
from . import views

urlpatterns = [
    path("get/", views.ProductClassView.as_view(), name="get_products"),
]

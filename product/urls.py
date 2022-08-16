from django.urls import path
from . import views

urlpatterns = [
    path("get", views.ProductsList.as_view(), name="get_products"),
    path("specific", views.GetSpecificProduct.as_view(), name="get_specific_products"),
]

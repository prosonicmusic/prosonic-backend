from nis import cat
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import traceback
from rest_framework import status, generics
from product.models import Product
from product.serializers import ProductSerializer
from prosonic_backend_core.utils import CustomResponse


# class ProductClassView(APIView):
#     # permission_classes = (IsAuthenticated,)

#     def get(self, request):
#         try:
#             pass
#         except Exception as e:
#             trace_back = traceback.format_exc()
#             message = str(e) + " " + str(trace_back)
#             return CustomResponse(
#                 self,
#                 status_code=500,
#                 errors=message,
#                 message="",
#                 data="",
#                 status=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             )


class ProductsList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsAuthenticated]

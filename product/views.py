from nis import cat
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import traceback
from rest_framework import status, generics
from product.models import Product
from product.serializers import ProductSerializer


class ProductClassView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            genres = request.GET["genres"]
            daw = request.GET["daw"]
            min_price = request.GET["minp"]
            max_price = request.GET["maxp"]
            product_type = request.GET["ptype"]

            return Response([], status=status.HTTP_200_OK)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + " " + str(trace_back)
            print(message)
            raise Exception(message)


# class ProductsList(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
# permission_classes = [IsAuthenticated]

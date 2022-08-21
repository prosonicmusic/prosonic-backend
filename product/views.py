from itertools import product
from nis import cat
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import traceback
from rest_framework import status, generics
from product.models import Product
from product.serializers import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404

from prosonic_backend_core.utils import customResponse


class ProductPageSizePagination(PageNumberPagination):
    page_size = 20


class ProductsList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["tag", "daw", "product_type", "genre"]
    pagination_class = ProductPageSizePagination
    permission_classes = []

    def get_queryset(self):
        queryset = Product.objects.all()
        min_price = self.request.GET.get("min_price")
        max_price = self.request.GET.get("max_price")

        if min_price:
            queryset = queryset.filter(product_price__gte=min_price)
        elif max_price:
            queryset = queryset.filter(product_price__lte=max_price)

        return queryset

    def create(self, request, *args, **kwargs):
        return customResponse(
            status=405, message="HTTP_405_METHOD_NOT_ALLOWED", success=0, data=[]
        )


class GetSpecificProduct(APIView):
    permission_classes = []

    def get(self, request):
        try:
            id = self.request.query_params.get("id")
            product = get_object_or_404(Product, pk=id)
            serialized_product = ProductSerializer(
                product, context={"request": request}
            )
            return customResponse(
                data=serialized_product.data, status=200, success=1, message=""
            )
        except Exception as e:
            print(e)
            raise e

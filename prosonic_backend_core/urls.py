from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

from user_profile.views import CustomTokenObtainPairView

schema_view = get_schema_view(
    openapi.Info(
        title="Prosonic API",
        default_version="v1",
        description="Feel free to test each api :D",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="mahmoudeslami@hotmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("login", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("user/", include("user_profile.urls")),
    path("product/", include("product.urls")),
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("ckeditor/", include("ckeditor_uploader.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

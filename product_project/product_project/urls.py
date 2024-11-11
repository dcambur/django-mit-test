from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("core.urls")),
    path("auth/", include("django.contrib.auth.urls")),
    path("auth/", include("product_auth.urls")),
    path("product/", include("product_management.urls")),
    path("admin/", admin.site.urls)
]

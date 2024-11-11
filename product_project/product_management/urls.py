from django.urls import path
from .views import *

urlpatterns = [
    path("list/", ProductList.as_view(), name="product_list"),
    path("create/", ProductCreate.as_view(), name="product_create"),
    path("<int:pk>/detail/", ProductDetail.as_view(), name="product_detail"),
    path("<int:pk>/update/", ProductUpdate.as_view(), name="product_update"),
    path("<int:pk>/delete/", ProductDelete.as_view(), name="product_delete"),
]

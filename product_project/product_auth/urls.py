from django.urls import path
from .views import *

urlpatterns = [
    path("", SignUpCreate.as_view(), name="sign_up"),
    path("user/<int:pk>/", UserProfileDetail.as_view(), name="user_profile_detail"),
    path("user/<int:pk>/update", UserProfileUpdate.as_view(), name="user_profile_update")
]

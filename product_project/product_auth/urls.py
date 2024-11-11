from django.urls import path
from .views import *

urlpatterns = [
    path("", SignUp.as_view(), name="sign_up"),
    path("user/<int:pk>/", UserProfileView.as_view(), name="user_profile")
]

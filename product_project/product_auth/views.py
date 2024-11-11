from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView
from .forms import NewUserCreationForm


class SignUp(CreateView, LoginRequiredMixin):
    form_class = NewUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class UserProfileView(DetailView):
    model = User
    success_url = reverse_lazy("login")
    template_name = "user_profile.html"
    context_object_name = "user_profile"

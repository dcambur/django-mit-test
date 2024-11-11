from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView
from .forms import NewUserCreationForm, UserProfileForm
from .models import UserProfile


class SignUpCreate(CreateView, LoginRequiredMixin):
    form_class = NewUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class UserProfileDetail(DetailView):
    model = UserProfile
    template_name = "user_profile_detail.html"
    context_object_name = "user_profile"


class UserProfileUpdate(UpdateView, LoginRequiredMixin):
    model = UserProfile
    form_class = UserProfileForm
    template_name = "user_profile_update.html"
    context_object_name = "user_profile"

    def get_success_url(self):
        return reverse_lazy('user_profile_detail', kwargs={"pk": self.object.pk})

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class NewUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Enter a valid email address.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class UserProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = UserProfile
        fields = ['location', 'birth_date', 'bio']

    def __init__(self, *args, **kwargs):
        user_profile = kwargs.get('instance')
        if user_profile:
            user = user_profile.user
            kwargs['initial'] = kwargs.get('initial', {})
            kwargs['initial']['username'] = user.username
            kwargs['initial']['email'] = user.email

        super().__init__(*args, **kwargs)
        self.reorder_form_fields()

    def reorder_form_fields(self):
        self.fields = {
            "username": self.fields['username'],
            "email": self.fields['email'],
            **{field: self.fields[field] for field in self.Meta.fields}
        }

    def save(self, commit=True):
        user = super().save(commit=False).user

        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
            super().save(commit=True)

        return user

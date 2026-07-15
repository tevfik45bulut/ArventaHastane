from django import forms
from apps.core.forms import BaseModelForm

from .models import User

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, EmailInput

from django.contrib.auth.forms import ReadOnlyPasswordHashField


class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        label="E-posta",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "E-posta",
                "autofocus": True,
            }
        ),
    )

    password = forms.CharField(
        label="Şifre",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Şifre",
            }
        ),
    )

    error_messages = {
        "invalid_login": "E-posta veya şifre hatalı.",
        "inactive": "Bu hesap pasif durumda.",
    }

class RegisterForm(BaseModelForm):

    password1 = forms.CharField(
        label="Şifre",
        widget=forms.PasswordInput,
    )

    password2 = forms.CharField(
        label="Şifre Tekrar",
        widget=forms.PasswordInput,
    )

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "phone_number",
        )

    def clean_email(self):
        email = self.cleaned_data["email"].lower()

        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                "Bu e-posta kullanılmaktadır."
            )

        return email

    def clean(self):
        cleaned = super().clean()

        if cleaned.get("password1") != cleaned.get("password2"):
            raise forms.ValidationError(
                "Şifreler uyuşmuyor."
            )

        return cleaned

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = (
            self.cleaned_data["email"]
            .strip()
            .lower()
        )
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()

        return user
    
class UserCreationForm(BaseModelForm):

    password1 = forms.CharField(
        label="Şifre",
        widget=forms.PasswordInput,
    )

    password2 = forms.CharField(
        label="Şifre Tekrar",
        widget=forms.PasswordInput,
    )

    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
        )

    def clean_password2(self):

        p1 = self.cleaned_data.get("password1")
        p2 = self.cleaned_data.get("password2")

        if p1 != p2:
            raise forms.ValidationError(
                "Şifreler uyuşmuyor."
            )

        return p2

    def save(self, commit=True):

        user = super().save(commit=False)

        user.set_password(
            self.cleaned_data["password1"]
        )

        if commit:
            user.save()

        return user

class UserChangeForm(BaseModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = "__all__"

    def clean_password(self):
        return self.initial["password"]
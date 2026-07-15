from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.views import (
    LoginView as DjangoLoginView,
    LogoutView as DjangoLogoutView,
)
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import LoginForm, RegisterForm


class LoginView(DjangoLoginView):

    template_name = "accounts/login.html"
    authentication_form = LoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("dashboard:index")


class LogoutView(DjangoLogoutView):

    next_page = reverse_lazy("website:home")


class RegisterView(CreateView):

    template_name = "accounts/register.html"

    form_class = RegisterForm

    success_url = reverse_lazy("dashboard:index")

    def form_valid(self, form):

        user = form.save()

        login(
            self.request,
            user,
            backend="apps.accounts.backends.EmailBackend",
        )

        messages.success(
            self.request,
            "Hesabınız oluşturuldu."
        )

        return redirect(self.success_url)
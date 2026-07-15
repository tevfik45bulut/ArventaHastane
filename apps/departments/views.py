from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .forms import DepartmentForm
from .models import Department


class DepartmentListView(LoginRequiredMixin, ListView):
    model = Department

    template_name = "departments/list.html"

    context_object_name = "departments"


class DepartmentCreateView(LoginRequiredMixin, CreateView):
    model = Department

    form_class = DepartmentForm

    template_name = "departments/form.html"

    success_url = reverse_lazy("departments:list")


class DepartmentUpdateView(LoginRequiredMixin, UpdateView):
    model = Department

    form_class = DepartmentForm

    template_name = "departments/form.html"

    success_url = reverse_lazy("departments:list")


class DepartmentDeleteView(LoginRequiredMixin, DeleteView):
    model = Department

    template_name = "departments/delete.html"

    success_url = reverse_lazy("departments:list")
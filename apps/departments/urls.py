from django.urls import path

from .views import (
    DepartmentCreateView,
    DepartmentDeleteView,
    DepartmentListView,
    DepartmentUpdateView,
)

app_name = "departments"

urlpatterns = [
    path(
        "",
        DepartmentListView.as_view(),
        name="list",
    ),

    path(
        "create/",
        DepartmentCreateView.as_view(),
        name="create",
    ),

    path(
        "<uuid:pk>/edit/",
        DepartmentUpdateView.as_view(),
        name="update",
    ),

    path(
        "<uuid:pk>/delete/",
        DepartmentDeleteView.as_view(),
        name="delete",
    ),
]
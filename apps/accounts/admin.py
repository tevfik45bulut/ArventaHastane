from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):

    add_form = UserCreationForm

    form = UserChangeForm

    model = User

    ordering = ("email",)

    list_display = (
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
        "date_joined",
    )

    list_filter = (
        "is_staff",
        "is_active",
        "is_superuser",
        "groups",
    )

    search_fields = (
        "email",
        "first_name",
        "last_name",
        "identity_number",
        "phone_number",
    )

    readonly_fields = (
        "date_joined",
        "last_login",
        "created_at",
        "updated_at",
    )

    fieldsets = (
        (
            "Giriş Bilgileri",
            {
                "fields": (
                    "email",
                    "password",
                )
            },
        ),
        (
            "Kişisel Bilgiler",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "phone_number",
                    "identity_number",
                    "birth_date",
                    "profile_photo",
                )
            },
        ),
        (
            "Yetkilendirme",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            "Sistem",
            {
                "fields": (
                    "last_login",
                    "date_joined",
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": (
                    "wide",
                ),
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                ),
            },
        ),
    )
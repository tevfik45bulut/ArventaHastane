from django.contrib import admin

from .models import (
    Doctor,
    DoctorWorkingHour,
    DoctorLeave,
)


class DoctorWorkingHourInline(admin.TabularInline):
    model = DoctorWorkingHour
    extra = 1
    min_num = 0


class DoctorLeaveInline(admin.TabularInline):
    model = DoctorLeave
    extra = 0


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "department",
        "title",
        "specialty",
        "is_active",
    )

    list_filter = (
        "department",
        "title",
        "is_active",
    )

    search_fields = (
        "user__first_name",
        "user__last_name",
        "user__email",
        "diploma_number",
    )

    autocomplete_fields = (
        "user",
        "department",
    )

    inlines = (
        DoctorWorkingHourInline,
        DoctorLeaveInline,
    )

    fieldsets = (
        (
            "Temel Bilgiler",
            {
                "fields": (
                    "user",
                    "department",
                    "title",
                    "specialty",
                    "diploma_number",
                )
            },
        ),
        (
            "Profil",
            {
                "fields": (
                    "photo",
                    "biography",
                )
            },
        ),
        (
            "Sistem",
            {
                "fields": (
                    "is_active",
                )
            },
        ),
    )
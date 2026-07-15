from django.db import models

from apps.accounts.models import User
from apps.core.models import BaseModel
from apps.departments.models import Department


class Doctor(BaseModel):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="doctor_profile",
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        related_name="doctors",
    )

    title = models.CharField(
        "Ünvan",
        max_length=50,
        default="Uzm. Dr.",
    )

    diploma_number = models.CharField(
        "Diploma No",
        max_length=50,
        unique=True,
    )

    specialty = models.CharField(
        "Uzmanlık",
        max_length=255,
    )

    biography = models.TextField(
        blank=True,
    )

    photo = models.ImageField(
        upload_to="doctors/",
        blank=True,
        null=True,
    )

    class Meta:
        ordering = (
            "user__first_name",
            "user__last_name",
        )

    def __str__(self):
        return f"{self.title} {self.user.full_name}"
    

class DoctorWorkingHour(BaseModel):

    WEEK_DAYS = (
        (1, "Pazartesi"),
        (2, "Salı"),
        (3, "Çarşamba"),
        (4, "Perşembe"),
        (5, "Cuma"),
        (6, "Cumartesi"),
        (7, "Pazar"),
    )

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name="working_hours",
    )

    weekday = models.PositiveSmallIntegerField(
        choices=WEEK_DAYS,
    )

    start_time = models.TimeField()

    end_time = models.TimeField()

    slot_duration = models.PositiveIntegerField(
        default=20,
        help_text="Dakika",
    )

    class Meta:
        ordering = (
            "weekday",
            "start_time",
        )

        unique_together = (
            "doctor",
            "weekday",
        )


class DoctorLeave(BaseModel):

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name="leaves",
    )

    start_date = models.DateField()

    end_date = models.DateField()

    reason = models.CharField(
        max_length=255,
        blank=True,
    )
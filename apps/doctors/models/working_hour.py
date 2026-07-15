from django.db import models

from apps.core.models import BaseModel
from .doctor import Doctor


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

    slot_duration = models.PositiveSmallIntegerField(
        default=20,
        help_text="Dakika",
    )

    class Meta:
        verbose_name = "Çalışma Saati"
        verbose_name_plural = "Çalışma Saatleri"
        ordering = (
            "doctor",
            "weekday",
            "start_time",
        )
        constraints = [
            models.UniqueConstraint(
                fields=["doctor", "weekday"],
                name="unique_doctor_weekday",
            )
        ]
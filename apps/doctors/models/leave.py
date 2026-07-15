from django.db import models

from apps.core.models import BaseModel
from .doctor import Doctor


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

    class Meta:
        verbose_name = "Doktor İzni"
        verbose_name_plural = "Doktor İzinleri"
        ordering = ("-start_date",)
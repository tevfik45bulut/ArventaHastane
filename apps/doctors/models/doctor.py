from django.db import models

from apps.accounts.models import User
from apps.core.models import BaseModel
from apps.departments.models import Department


class Doctor(BaseModel):

    TITLES = (
        ("prof", "Prof. Dr."),
        ("assoc", "Doç. Dr."),
        ("assist", "Dr. Öğr. Üyesi"),
        ("specialist", "Uzm. Dr."),
        ("gp", "Pratisyen Hekim"),
    )

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
        max_length=20,
        choices=TITLES,
        default="specialist",
    )

    diploma_number = models.CharField(
        max_length=50,
        unique=True,
    )

    specialty = models.CharField(
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
        verbose_name = "Doktor"
        verbose_name_plural = "Doktorlar"
        ordering = (
            "user__first_name",
            "user__last_name",
        )

    @property
    def full_title(self):
        return f"{self.get_title_display()} {self.user.full_name}"

    def __str__(self):
        return self.full_title
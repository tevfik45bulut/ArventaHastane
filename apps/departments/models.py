from django.db import models
from django.utils.text import slugify

from apps.core.models import BaseModel


class Department(BaseModel):
    code = models.CharField(
        "Kod",
        max_length=10,
        unique=True,
        db_index=True,
    )

    name = models.CharField(
        "Bölüm Adı",
        max_length=150,
        unique=True,
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
    )

    description = models.TextField(
        "Açıklama",
        blank=True,
    )

    icon = models.CharField(
        "Bootstrap Icon",
        max_length=50,
        default="bi-hospital",
    )

    phone = models.CharField(
        "Telefon",
        max_length=20,
        blank=True,
    )

    email = models.EmailField(
        "E-posta",
        blank=True,
    )

    floor = models.CharField(
        "Kat / Blok",
        max_length=50,
        blank=True,
    )

    order = models.PositiveIntegerField(
        "Sıralama",
        default=0,
    )

    class Meta:
        db_table = "departments"
        verbose_name = "Bölüm"
        verbose_name_plural = "Bölümler"
        ordering = ["order", "name"]

    def __str__(self):
        return f"{self.code} - {self.name}"

    def save(self, *args, **kwargs):
        self.code = self.code.strip().upper()

        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)
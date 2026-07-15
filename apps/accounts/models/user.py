from __future__ import annotations

import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone

from apps.accounts.managers import UserManager
from apps.core.validators import validate_identity_number


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    email = models.EmailField(
        "E-posta",
        unique=True,
        db_index=True,
    )

    first_name = models.CharField(
        "Ad",
        max_length=100,
    )

    last_name = models.CharField(
        "Soyad",
        max_length=100,
    )

    identity_number = models.CharField(
        "TC Kimlik No",
        max_length=11,
        unique=True,
        validators=[validate_identity_number],
        blank=True,
        null=True,
    )

    phone_number = models.CharField(
        "Telefon",
        max_length=20,
        blank=True,
    )

    birth_date = models.DateField(
        "Doğum Tarihi",
        blank=True,
        null=True,
    )

    profile_photo = models.ImageField(
        "Profil Fotoğrafı",
        upload_to="profiles/",
        blank=True,
        null=True,
    )

    is_active = models.BooleanField(default=True)

    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
    ]

    class Meta:
        db_table = "users"
        ordering = ["first_name", "last_name"]
        verbose_name = "Kullanıcı"
        verbose_name_plural = "Kullanıcılar"

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return self.full_name
    
    def save(self, *args, **kwargs):
        if self.email:
            self.email = self.__class__.objects.normalize_email(
                self.email.strip()
            ).lower()

        super().save(*args, **kwargs)
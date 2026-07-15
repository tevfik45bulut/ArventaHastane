from __future__ import annotations

from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email: str, password: str | None = None, **extra_fields):
        if not email:
            raise ValueError("Email alanı zorunludur.")

        email = self.normalize_email(email)

        email = email.strip().lower()

        user = self.model(
            email=email,
            **extra_fields,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if not extra_fields["is_staff"]:
            raise ValueError("is_staff=True olmalıdır.")

        if not extra_fields["is_superuser"]:
            raise ValueError("is_superuser=True olmalıdır.")

        return self.create_user(
            email=email,
            password=password,
            **extra_fields,
        )
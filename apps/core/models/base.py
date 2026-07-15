import uuid

from django.db import models
from django.utils import timezone

from .managers import ActiveManager, AllObjectsManager


class TimeStampedModel(models.Model):
    """
    Adds created_at and updated_at fields.
    """

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Oluşturulma Tarihi",
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Güncellenme Tarihi",
    )

    class Meta:
        abstract = True


class BaseModel(TimeStampedModel):
    """
    Base model for business entities.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    is_active = models.BooleanField(
        default=True,
        db_index=True,
        verbose_name="Aktif",
    )

    objects = ActiveManager()
    all_objects = AllObjectsManager()

    class Meta:
        abstract = True
        ordering = ("-created_at",)


class SoftDeleteModel(BaseModel):
    """
    Adds soft delete support.
    """

    is_deleted = models.BooleanField(
        default=False,
        db_index=True,
    )

    deleted_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save(update_fields=["is_deleted", "deleted_at"])

    def restore(self):
        self.is_deleted = False
        self.deleted_at = None
        self.save(update_fields=["is_deleted", "deleted_at"])

    def hard_delete(self):
        return super().delete()
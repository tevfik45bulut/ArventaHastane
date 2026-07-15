from django.db import models


class ActiveManager(models.Manager):
    """
    Returns only active and non deleted objects.
    """

    def get_queryset(self):
        queryset = super().get_queryset()

        fields = {field.name for field in self.model._meta.fields}

        if "is_deleted" in fields:
            queryset = queryset.filter(is_deleted=False)

        if "is_active" in fields:
            queryset = queryset.filter(is_active=True)

        return queryset


class AllObjectsManager(models.Manager):
    """
    Returns every object.
    """

    pass
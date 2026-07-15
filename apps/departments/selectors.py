from .models import Department


def get_active_departments():
    """
    Return active departments ordered by display order.
    """
    return Department.objects.order_by("order", "name")


def get_department_by_slug(slug: str):
    return Department.objects.get(
        slug=slug,
        is_active=True,
    )
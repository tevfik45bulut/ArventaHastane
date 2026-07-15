from .models import Department


def create_department(**data):
    """
    Create a department.
    """
    return Department.objects.create(**data)


def update_department(department, **data):
    """
    Update department fields.
    """
    for key, value in data.items():
        setattr(department, key, value)

    department.save()

    return department
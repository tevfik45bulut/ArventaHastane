from apps.core.forms import BaseModelForm

from .models import Department


class DepartmentForm(BaseModelForm):

    class Meta:
        model = Department

        fields = (
            "code",
            "name",
            "description",
            "icon",
            "phone",
            "email",
            "floor",
            "order",
            "is_active",
        )
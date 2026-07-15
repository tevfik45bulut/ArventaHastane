from django import forms


class BaseForm(forms.Form):
    """
    Automatically styles widgets with Bootstrap 5.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            widget = field.widget

            if isinstance(widget, forms.CheckboxInput):
                css = "form-check-input"

            elif isinstance(widget, forms.Select):
                css = "form-select"

            else:
                css = "form-control"

            widget.attrs.setdefault("class", css)
            widget.attrs.setdefault(
                "placeholder",
                field.label or "",
            )


class BaseModelForm(forms.ModelForm):
    """
    Base model form.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            widget = field.widget

            if isinstance(widget, forms.CheckboxInput):
                css = "form-check-input"

            elif isinstance(widget, forms.Select):
                css = "form-select"

            else:
                css = "form-control"

            widget.attrs.setdefault("class", css)
            widget.attrs.setdefault(
                "placeholder",
                field.label or "",
            )
from django.core.exceptions import ValidationError


def validate_identity_number(value: str):
    """
    Basic Turkish identity number validation.
    Advanced checksum validation will be added later.
    """

    if not value.isdigit():
        raise ValidationError("TC Kimlik No sadece rakamlardan oluşmalıdır.")

    if len(value) != 11:
        raise ValidationError("TC Kimlik No 11 haneli olmalıdır.")
from django.db import models


class UserRole(models.TextChoices):
    ADMIN = "ADMIN", "Yönetici"
    DOCTOR = "DOCTOR", "Doktor"
    SECRETARY = "SECRETARY", "Sekreter"
    PATIENT = "PATIENT", "Hasta"
    LABORATORY = "LABORATORY", "Laboratuvar"
    PHARMACY = "PHARMACY", "Eczane"


class Gender(models.TextChoices):
    MALE = "M", "Erkek"
    FEMALE = "F", "Kadın"
    OTHER = "O", "Diğer"
from datetime import datetime, timedelta

from .models import Doctor, DoctorWorkingHour

def get_working_hour(doctor: Doctor, date):
    """
    Return doctor's working hours for the given date.
    """

    weekday = date.isoweekday()

    return DoctorWorkingHour.objects.filter(
        doctor=doctor,
        weekday=weekday,
        is_active=True,
    ).first()


def generate_slots(doctor: Doctor, date):
    """
    Generate available appointment slots.
    """

    working_hour = get_working_hour(
        doctor,
        date,
    )

    if not working_hour:
        return []

    start = datetime.combine(
        date,
        working_hour.start_time,
    )

    end = datetime.combine(
        date,
        working_hour.end_time,
    )

    duration = timedelta(
        minutes=working_hour.slot_duration,
    )

    slots = []

    while start < end:

        slots.append(
            start.time()
        )

        start += duration

    return slots


def get_available_slots(
    doctor,
    date,
):
    """
    Return available appointment slots.

    Appointment integration will be added in Sprint 3.
    """

    return generate_slots(
        doctor,
        date,
    )



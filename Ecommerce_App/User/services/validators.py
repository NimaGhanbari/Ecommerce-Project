# Django
from django.core.exceptions import ValidationError

# Python
import re


def ValidatorPhoneNumber(value: int) -> None:
    pattern = r'^989\d{9}$'
    if not re.match(pattern, str(value)):
        raise ValidationError("Please enter a valid phone number")

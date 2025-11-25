from django.core.exceptions import ValidationError
import re

def validate_name(name:str) -> str | ValidationError:
    if re.search(r'^\w+ \w\. \w+$', name):
        return name
    raise ValidationError('Name must be in the format "First Middle Initial. Last"')

def validate_email(email:str) -> str | ValidationError:
    if re.search(r'^[A-Za-z0-9._-]+@school\.com$', email):
        return email
    raise ValidationError('Invalid school email format. Please use an email ending with "@school.com".')

def validate_locker_combination(locker_combination):
    if re.search(r'^\d{2}-\d{2}-\d{2}$', locker_combination):
        return locker_combination
    raise ValidationError('Combination must be in the format "12-12-12"')
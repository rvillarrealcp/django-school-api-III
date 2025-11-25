from django.db import models
from django.utils import timezone
from django.core import validators as v
from .validators import validate_name, validate_email, validate_locker_combination
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, validators=[validate_name])
    student_email = models.EmailField(null=False, blank=False, unique=True, validators=[validate_email] )
    personal_email = models.EmailField(null=False, blank=False, unique=True)
    locker_number = models.IntegerField(default=110, null=False, blank=False, unique=True, validators=[v.MinValueValidator(1), v.MaxValueValidator(200)])
    locker_combination = models.CharField( default="12-12-12",null=False, blank=False,max_length=255, validators=[validate_locker_combination])
    good_student = models.BooleanField(default=True)
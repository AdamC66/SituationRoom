from django.contrib.auth.models import AbstractUser
from django.db import models
from situationroom.utils.helpers import code_generator

def user_code_generator():
    return code_generator("USR", 20)
class SituationRoomUser(AbstractUser):
    code = models.CharField(max_length=30, unique=True, default=user_code_generator)
    # Personal Info
    title = models.CharField(max_length=255, blank=True, null=True)
    designations = models.CharField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    avatar = models.URLField(null=True, blank=True)
    # Address
    address_line_1 = models.CharField(max_length=500, blank=True, null=True)
    address_line_2 = models.CharField(max_length=500, blank=True, null=True)
    address_city = models.CharField(max_length=50, blank=True, null=True)
    address_state = models.CharField(max_length=50, blank=True, null=True)
    address_zip = models.CharField(max_length=10, blank=True, null=True)
    address_country = models.CharField(max_length=50, blank=True, null=True)
    address_phone = models.CharField(max_length=15, blank=True, null=True)

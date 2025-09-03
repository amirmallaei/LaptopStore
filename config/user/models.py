from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core import Validators
import uuid

# Create your models here.
class UserModel(AbstractUser):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    mobile = models.BigIntegerField(unique =True, verbose_name="Phone Number", 
    validators = [Validators.RegexValidator(regex=r'9[0-3,9]\d{8}$')],
    error_messages = {'unique':("A User With this phone number existes"),})
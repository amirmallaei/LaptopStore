from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.contrib.auth.models import BaseUserManager
import uuid


class UserManager(BaseUserManager):
    """Custom manager for UserModel with email as username field."""

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # hash password
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """
        Create and save a regular user.
        """
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and save a superuser.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class UserModel(AbstractUser):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    mobile = models.BigIntegerField(unique =True, verbose_name="Phone Number", 
    validators = [validators.RegexValidator(regex=r'9[0-3,9]\d{8}$')],
    error_messages = {'unique':("A User With this phone number existes"),})
    first_name = models.CharField(max_length=30, verbose_name="First Name")
    last_name = models.CharField(max_length=30, verbose_name="Last Name")
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_created=True, null=True, blank=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['mobile']

    objects = UserManager()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    

class Profile(models.Model):
    GENDER_CHOICE = (
        (0, "NOT SELECTED"),
        (1, "MALE"),
        (2, "FEMALE")
    )
    ROLE_CHOICE = (
        (0, "USER"),
        (1, "ADMIN")
    )
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name="profile") 
    role = models.IntegerField(default=0, choices=ROLE_CHOICE)
    gender = models.IntegerField(default=0, choices=GENDER_CHOICE)
    address = models.TextField(blank=True, null=True)

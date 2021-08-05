from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

import uuid

class UserManager(BaseUserManager):
    def _create_user(self, phone_number, password, **extra_fields):
        if not phone_number:
            raise ValueError("The given phone number must be set")

        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone_number, password, **extra_fields)

    def create_superuser(self, phone_number, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(phone_number, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    guid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    phone_number = PhoneNumberField(
        "Phone number",
        unique=True,
        help_text="Required. Only international format used.",
        error_messages={
            "unique": "User with this phone number already exists."
        },
    )
    first_name = models.CharField("first name", max_length=150, blank=True)
    last_name = models.CharField("last name", max_length=150, blank=True)
    date_joined = models.DateTimeField("date joined", auto_now_add=True)
    is_staff = models.BooleanField('staff status', default=False)

    objects = UserManager()

    USERNAME_FIELD = "phone_number"

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.phone_number}"

    @property
    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def update_profile(self, validated_data):
        self.first_name = validated_data.get("first_name", self.first_name)
        self.last_name = validated_data.get("last_name", self.last_name)
        self.save()
        return self
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_seller = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    username = models.CharField(max_length=150, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
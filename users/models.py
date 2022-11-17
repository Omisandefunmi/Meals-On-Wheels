import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class User(AbstractUser):

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    country = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=25, blank=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "username", "phone"]


    def __str__(self) -> str:
        return self.email


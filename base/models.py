from django.contrib.auth.models import AbstractUser , Group , Permission
from django.db import models

class User(AbstractUser):
    username = models.CharField(max_length=256, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    password = models.CharField(max_length=256, null=False, blank=False)
    is_admin = models.BooleanField(default=False)

    REQUIRED_FIELDS = []
    groups = models.ManyToManyField(
        Group,
        related_name = "users",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name = "users",
    )
    def __str__(self):
        return self.username

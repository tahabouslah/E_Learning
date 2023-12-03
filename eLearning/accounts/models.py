from django.contrib.auth.models import AbstractUser
from django.db import models

ROLE_CHOICES = [
        ("Student", "Student"),
        ("Tutor", "Tutor"),
        ("Administrator", "Administrator"),
    ]

class CustomUser(AbstractUser):
    role = models.CharField(max_length=255, choices=ROLE_CHOICES)
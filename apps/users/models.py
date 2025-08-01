from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    full_name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    school = models.TextField(null=True)
    school_class = models.TextField(null=True)
    address = models.TextField(null=True)

    first_name = None
    last_name = None

    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return self.full_name


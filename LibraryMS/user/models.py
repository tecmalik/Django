from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=11, unique=True)


class Author(User):
    dob = models.DateField(blank=False, null=False)
    dod = models.DateField(blank=True, null= True)
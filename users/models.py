from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    status = models.CharField(max_length=1)
    cnpj = models.CharField(max_length=20)
    nome = models.CharField(max_length=255)

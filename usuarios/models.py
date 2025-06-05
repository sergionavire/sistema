from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    # Ejemplo de campo adicional
    bio = models.TextField(blank=True, null=True)
    email = models.EmailField(
        unique=True,
        error_messages={
            'unique': "Já existe um usuário com este e-mail.",
        }
    )

    def __str__(self):
        return self.username

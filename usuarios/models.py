from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    """
    Modelo personalizado de usuario que hereda de AbstractUser.
    Puedes agregar campos adicionales si es necesario.
    """
    # Ejemplo de campo adicional
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username

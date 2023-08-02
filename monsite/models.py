from django.core.validators import RegexValidator
from django.db import models

# Create your models here.

class Service(models.Model):
    nom = models.CharField(max_length=255)
    image = models.ImageField()
    descrption = models.TextField()

class Utilisateur(models.Model):
    nom = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    telephone = models.CharField(
        max_length=16,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format '+123456789'. Up to 15 digits allowed."
            ),
        ],
    )
    sujet = models.CharField()
    message = models.TextField()

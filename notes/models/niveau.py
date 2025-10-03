from django.core.exceptions import ValidationError
from django.db import models

def nom_vide(value):
    if not value.strip():
        raise ValidationError("Le nom ne peut pas être vide ou uniquement des espaces.")

class Niveau(models.Model):
    nom = models.CharField(
        max_length=2, 
        unique=True, 
        blank=False,
        validators=[nom_vide] 
    )

    class Meta:
        verbose_name = "Niveau"
        verbose_name_plural = "Niveaux"

    def __str__(self):
        return self.nom


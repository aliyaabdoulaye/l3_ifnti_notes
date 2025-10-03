from django.db import models

from .personne import Personne
from .niveau import Niveau

class Eleve(Personne):
    matricule = models.CharField(max_length=20, unique=True)
    # Un élève appartient à un niveau
    niveau = models.ForeignKey(
        Niveau,
        on_delete=models.CASCADE, 
        related_name='eleves'
    )

    def __str__(self):
        return f"{self.prenom} {self.nom}"

    class Meta:
        verbose_name = "Élève"
        verbose_name_plural = "Élèves"


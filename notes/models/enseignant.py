from django.db import models
from .personne import Personne

class Enseignant(Personne):
    # Un enseignant peut enseigner plusieurs matières
    # La relation est définie dans le modèle Matiere

    class Meta:
        verbose_name = "Enseignant"
        verbose_name_plural = "Enseignants"

    def __str__(self):
        return f"{self.prenom} {self.nom}"


from django.db import models
from .niveau import Niveau

class Matiere(models.Model):
    nom = models.CharField(max_length=50, unique=True)
    # Une matière peut être enseignée dans plusieurs niveaux (1 à 3)
    niveaux = models.ManyToManyField(Niveau, related_name='matieres')
    # Une matière a un seul enseignant
    enseignant = models.ForeignKey(
        'Enseignant', 
        on_delete=models.CASCADE, 
        related_name='matieres_enseignees'
    )

    class Meta:
        verbose_name = "Matière"
        verbose_name_plural = "Matières"

    def __str__(self):
        return self.nom


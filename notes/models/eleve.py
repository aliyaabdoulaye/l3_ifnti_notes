from django.db import models
from .personne import Personne
from .niveau import Niveau

class Eleve(Personne):
    matricule = models.CharField(max_length=20, unique=True)

    niveau = models.ForeignKey(
        Niveau,
        on_delete=models.CASCADE,
        related_name='eleves'
    )
    matieres = models.ManyToManyField(
        'Matiere',
        related_name='eleves_inscrits',
        blank=True,
        verbose_name="Matières suivies"
    )
    
    class Meta:
        verbose_name = "Élève"
        verbose_name_plural = "Élèves"
    
    def __str__(self):
        return f"{self.prenom} {self.nom}"
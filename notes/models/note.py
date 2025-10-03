from django.db import models
from .eleve import Eleve
from .matiere import Matiere

class Note(models.Model):
    valeur = models.FloatField(null=True, blank=True)
    # Une note appartient a un eleve
    eleve = models.ForeignKey(
        Eleve, 
        on_delete=models.CASCADE, 
        related_name='notes'
    )
    # Une note concerne une matiere
    matiere = models.ForeignKey(
        Matiere, 
        on_delete=models.CASCADE, 
        related_name='notes'
    )
    
    class Meta:
        # Contrainte : un eleve ne peut avoir qu'une note par matiere
        unique_together = ('eleve', 'matiere')
    
    def __str__(self):
        return f"{self.eleve} - {self.matiere}: {self.valeur}"
        
 

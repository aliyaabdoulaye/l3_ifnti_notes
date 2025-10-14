from django.shortcuts import render
from django.db.models import Avg, Count
from notes.models import Eleve, Note, Niveau, Matiere, Enseignant

def statistiques(request, niveau_id=None):
   
    
    nb_eleves = Eleve.objects.count()
    nb_enseignants = Enseignant.objects.count()
    nb_matieres = Matiere.objects.count()
    nb_notes = Note.objects.count()
    
    if niveau_id:
        eleves = Eleve.objects.filter(niveau_id=niveau_id)
        niveau_filtre = Niveau.objects.get(id=niveau_id)
    else:
        eleves = Eleve.objects.all()
        niveau_filtre = None
    

    moyenne1 = eleves.annotate(
        moyenne_generale=Avg('notes__valeur')
    ).order_by('-moyenne_generale')
    
    moyenne_mat = Matiere.objects.annotate(
        moyenne_matiere=Avg('notes__valeur')
    ).filter(moyenne_matiere__isnull=False).order_by('nom')
    
    eleves_5_premier = eleves.annotate(
        moyenne_generale=Avg('notes__valeur')
    ).filter(
        moyenne_generale__isnull=False
    ).order_by('-moyenne_generale')[:5]
    
    statistique_niveau = Niveau.objects.annotate(
        nombre_eleves=Count('eleves'),
        moyenne_niveau=Avg('eleves__notes__valeur')
    ).order_by('nom')
    
    context = {
        'nb_eleves': nb_eleves,
        'nb_enseignants': nb_enseignants,
        'nb_matieres': nb_matieres,
        'nb_notes': nb_notes,
        'moyenne1': moyenne1,
        'moyenne_mat': moyenne_mat,
        'eleves_5_premier': eleves_5_premier,
        'statistique_niveau': statistique_niveau,
        'niveau_filtre': niveau_filtre,
        'tous_niveaux': Niveau.objects.all(),
    }
    
    return render(request, 'notes/statistiques.html', context)

















































    #path('statistiques/<int:niveau_id>/', views.statistiques, name='statistiques_niveau'),

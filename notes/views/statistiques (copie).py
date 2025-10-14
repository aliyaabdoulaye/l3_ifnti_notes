from django.shortcuts import render
from django.db.models import Avg, Count, Q
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
    
    eleves_avec_moyenne = eleves.annotate(
        moyenne_generale=Avg('notes__valeur')
    ).order_by('-moyenne_generale')
    
    matieres_avec_moyenne = Matiere.objects.annotate(
        moyenne_matiere=Avg('notes__valeur')
    ).filter(moyenne_matiere__isnull=False).order_by('nom')
    
    top_5_eleves = eleves.annotate(
        moyenne_generale=Avg('notes__valeur')
    ).filter(
        moyenne_generale__isnull=False
    ).order_by('-moyenne_generale')[:5]
    
    niveaux_stats = Niveau.objects.annotate(
        nombre_eleves=Count('eleves'),
        moyenne_niveau=Avg('eleves__notes__valeur')
    ).order_by('nom')
    
    context = {
        'nb_eleves': nb_eleves,
        'nb_enseignants': nb_enseignants,
        'nb_matieres': nb_matieres,
        'nb_notes': nb_notes,
        'eleves_avec_moyenne': eleves_avec_moyenne,
        'matieres_avec_moyenne': matieres_avec_moyenne,
        'top_5_eleves': top_5_eleves,
        'niveaux_stats': niveaux_stats,
        'niveau_filtre': niveau_filtre,
        'tous_niveaux': Niveau.objects.all(),
    }
    
    return render(request, 'notes/statistiques.html', context)

















































    #path('statistiques/<int:niveau_id>/', views.statistiques, name='statistiques_niveau'),

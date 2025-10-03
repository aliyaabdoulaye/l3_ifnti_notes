from django.shortcuts import render, get_object_or_404

from notes.models import Matiere

def matieres(request):
    liste_matieres = Matiere.objects.all()
    context = {'matieres': liste_matieres}
    return render(request, 'notes/matieres.html', context)

def matiere(request, matiere_id):
    matiere_obj = get_object_or_404(Matiere, pk=matiere_id)
    context = {'matiere': matiere_obj}
    return render(request, 'notes/matiere.html', context)

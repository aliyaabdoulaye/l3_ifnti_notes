from django.shortcuts import render
from notes.models import Enseignant

def enseignants(request):
    liste_enseignants = Enseignant.objects.all()
    context = {'enseignants': liste_enseignants}
    return render(request, 'notes/enseignants.html', context)

from django.shortcuts import render, get_object_or_404
from notes.models import Eleve

def eleves(request):
    liste_eleves = Eleve.objects.all()
    context = {'eleves': liste_eleves}
    return render(request, 'notes/eleves.html', context)

def eleve(request, eleve_id):
    eleve_obj = get_object_or_404(Eleve, pk=eleve_id)
    context = {'eleve': eleve_obj}
    return render(request, 'notes/eleve.html', context)

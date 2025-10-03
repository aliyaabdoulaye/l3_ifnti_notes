from django.shortcuts import render, get_object_or_404

from notes.models import Niveau

def niveau(request, niveau_id):
    niveau_obj = get_object_or_404(Niveau, pk=niveau_id)
    context = {'niveau': niveau_obj}
    return render(request, 'notes/niveau.html', context)

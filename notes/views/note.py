from django.shortcuts import render
from notes.models import Note

def note(request):
    liste_notes = Note.objects.all()
    context = {'note': liste_notes}
    return render(request, 'notes/note.html', context)

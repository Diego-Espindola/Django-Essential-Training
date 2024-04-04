from django.shortcuts import render

from .models import Notes


def list_items(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': all_notes})

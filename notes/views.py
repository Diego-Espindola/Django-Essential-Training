from django.shortcuts import render
from django.http import Http404

from .models import Notes


def list_items(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': all_notes})


def detail(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        # raise Http404("Note doesn't exist")
        url = request.build_absolute_uri()
        return render(request, 'notes/404_error.html', {'pk': pk, 'url': url})
    return render(request, 'notes/notes_detail.html', {'note': note})

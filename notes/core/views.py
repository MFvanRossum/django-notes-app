from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse
from .models import Note
from .forms import NoteForm

def notes_detail(request, pk):
    note = Note.objects.get(pk=pk)
    notes = Note.objects.all()
    return render(request, 'core/notes_detail.html', {'notes': notes, 'note': note, "pk": pk})

def note_new(request):
    notes = Note.objects.all()
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes-list')
    else:
        form = NoteForm()
    return render(request, 'core/post_edit.html', {'notes': notes, 'form': form})

def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)
    notes = Note.objects.all()
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes-list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'core/post_edit.html', {'notes': notes, 'form': form})

def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect('notes-list')
from django.shortcuts import render, redirect
from .models import Note
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify

@login_required(login_url="/users/login/")
def notes_list(request):
    notes = Note.objects.all().order_by('-date')
    return render(request, 'notes/notes_list.html', {'notes': notes})

def note_page(request, slug):
    note = Note.objects.get(slug=slug)
    return render(request, 'notes/note_page.html', {'note': note})

@login_required(login_url="/users/login/")
def new_note(request):
    if request.method == "POST":
        title = request.POST.get("title")
        body = request.POST.get("body")

        slug = slugify(title)

        note = Note.objects.create(
            title=title,
            body=body,
            slug=slug
        )

        return redirect("notes:list")

    return render(request, 'notes/new_note.html')

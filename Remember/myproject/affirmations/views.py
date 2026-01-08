from django.shortcuts import render
from .models import Affirmation
from django.contrib.auth.decorators import login_required

# Create your views here.
#@login_required(login_url="/users/login/")
def affirmations_list(request):
    affirmations = Affirmation.objects.all().order_by('-date')
    return render(request, 'affirmations/affirmations_list.html', {'affirmations': affirmations})

def affirmation_page(request, slug):
    affirmation = Affirmation.objects.get(slug=slug)
    return render(request, 'affirmations/affirmation_page.html', {'affirmation': affirmation})
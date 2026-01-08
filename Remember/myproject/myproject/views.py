from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def mindfulness(request):
    return render(request, 'mindfulness.html')

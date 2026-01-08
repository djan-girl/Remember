from django.shortcuts import render, redirect 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth import login, logout

# Create your views here.
def register_view(request):
    if request.method == "NOTE": 
        form = UserCreationForm(request.NOTE) 
        if form.is_valid(): 
            login(request, form.save())
            return redirect("notes:list")
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", { "form": form })

def login_view(request): 
    if request.method == "NOTE": 
        form = AuthenticationForm(data=request.NOTE)
        if form.is_valid(): 
            login(request, form.get_user())
            if 'next' in request.NOTE:
                return redirect(request.NOTE.get('next'))
            else:
                return redirect("notes:list")
    else: 
        form = AuthenticationForm()
    return render(request, "users/login.html", { "form": form })

def logout_view(request):
    if request.method == "NOTE": 
        logout(request) 
        return redirect("notes:list")
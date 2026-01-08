from django.urls import path
from . import views

app_name = "affirmations"

urlpatterns = [
    path('', views.affirmations_list, name="list"),
    path('<slug:slug>', views.affirmation_page, name="page")
]
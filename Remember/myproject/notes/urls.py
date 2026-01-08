from django.urls import path
from . import views

app_name = "notes"

urlpatterns = [
    path('', views.notes_list, name="list"),
    path('new_post/', views.new_note, name="new_note"),
    path('<slug:slug>/', views.note_page, name="page"),
]

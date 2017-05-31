from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Film
# Create your views here.

class FilmListView(ListView):
    model = Film

class FilmDetailView(DetailView):
    model = Film
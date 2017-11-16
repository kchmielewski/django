from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Director, Film
from django.http import HttpResponse

# Create your views here.

class MainPageView(TemplateView):
    template_name= 'index.html'

class DirectorListView(ListView):
    model = Director

class DirectorDetailView(DetailView):
    model = Director

class FilmListView(ListView):
    model = Film

class FilmDetailView(DetailView):
    model = Film


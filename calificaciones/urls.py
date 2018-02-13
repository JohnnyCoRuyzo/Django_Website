from django.conf.urls import url, include 
from django.views.generic import ListView, DetailView
from calificaciones.models import Semestres
from calificaciones.views import ListaSemestres, ListaMaterias,ListaNotas,ListaSubNotas

urlpatterns = [
    url(r'^$', view = ListaSemestres, name = "Lista de Semestres"),
    url(r'^(?P<numero>(\d+))/$', view = ListaMaterias, name = "Lista de materias"),
    url(r'^(?P<numero>(\d+))/(?P<codigo>(\d+))/$', view = ListaNotas, name = "Lista de Notas"),
    url(r'^(?P<numero>(\d+))/(?P<codigo>(\d+))/(?P<id>(\d+))/$', view = ListaSubNotas, name = "Lista de SubNotas")
]
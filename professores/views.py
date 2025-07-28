from django.shortcuts import render
from django.views.generic import ListView
from professores.models import ProfessoresModel
from django.views.generic import ListView

class ProfessorListView(ListView):
    model = ProfessoresModel
    template_name = 'professores/lista.html'
    context_object_name = 'professores'

class DetalheProfessorListView(ListView):
    model = ProfessoresModel
    template_name = 'professores/detalhe.html'
    context_object_name = 'professores'

class FormularioProfessorListView(ListView):
    model = ProfessoresModel
    template_name = 'professores/formulario.html'
    context_object_name = 'professores'

class DeletarProfessorListView(ListView):
    model = ProfessoresModel
    template_name = 'professores/deletar.html'
    context_object_name = 'professores'

from django.shortcuts import render
from alunos.models import AlunosModel
from django.views.generic import ListView

class AlunosListView(ListView):
    model = AlunosModel
    template_name = 'alunos/lista.html'
    context_object_name = 'alunos'

class DetalheAlunoListView(ListView):
    model = AlunosModel
    template_name = 'alunos/detalhe.html'
    context_object_name = 'alunos'

class FormularioAlunoListView(ListView):
    model = AlunosModel
    template_name = 'alunos/formulario.html'
    context_object_name = 'alunos'

class DeletarAlunoListView(ListView):
    model = AlunosModel
    template_name = 'alunos/deletar.html'
    context_object_name = 'alunos'

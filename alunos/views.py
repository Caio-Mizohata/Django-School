from django.shortcuts import render
from alunos.models import AlunosModel
from alunos.forms import AlunoForm, EscolaForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView

class AlunosListView(ListView):
    model = AlunosModel
    template_name = 'alunos/lista.html'
    context_object_name = 'alunos'

class DetalheAlunoListView(ListView):
    model = AlunosModel
    template_name = 'alunos/detalhe.html'
    context_object_name = 'alunos'

class FormularioAlunoListView(CreateView):
    model = AlunosModel
    template_name = 'alunos/formulario.html'
    form_class = AlunoForm
    success_url = reverse_lazy('listar_alunos')

class DeletarAlunoListView(ListView):
    model = AlunosModel
    template_name = 'alunos/deletar.html'
    sucess_url = reverse_lazy('listar_alunos')


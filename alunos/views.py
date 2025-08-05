from django.shortcuts import render
from alunos.models import AlunosModel
from alunos.forms import AlunoForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView

class AlunosListView(ListView):
    model = AlunosModel
    template_name = 'alunos/lista.html'
    context_object_name = 'alunos'

class DetalheAlunoDetailView(DetailView):
    model = AlunosModel
    template_name = 'alunos/detalhe.html'
    context_object_name = 'aluno'

class FormularioAlunoCreateView(CreateView):
    template_name = 'alunos/formulario.html'
    form_class = AlunoForm
    success_url = reverse_lazy('listar_alunos')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_name'] = 'aluno_form'
        return context

class EditarAlunoView(UpdateView):
    model = AlunosModel
    form_class = AlunoForm
    template_name = 'alunos/formulario.html'
    success_url = reverse_lazy('listar_alunos')

class DeletarAlunoDeleteView(DeleteView):
    model = AlunosModel
    template_name = 'alunos/deletar.html'
    success_url = reverse_lazy('listar_alunos')
    context_object_name = 'aluno'

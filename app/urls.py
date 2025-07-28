from django.contrib import admin
from django.urls import path
from core.views import AboutListView, ContactListView, HomeListView
from alunos.views import AlunosListView, DetalheAlunoListView, FormularioAlunoListView, DeletarAlunoListView
from professores.views import ProfessorListView, DetalheProfessorListView, FormularioProfessorListView, DeletarProfessorListView

urlpatterns = [
    path('admin/', admin.site.urls),
    # Página principal
    path('', HomeListView.as_view(), name='home'),
    path('sobre/', AboutListView.as_view(), name='about'),
    path('contato/', ContactListView.as_view(), name='contact'),
    # Página de Alunos
    path('alunos/list', AlunosListView.as_view(), name='listar_alunos'),
    path('alunos/detalhe', DetalheAlunoListView.as_view(), name='detalhe_aluno'),
    path('alunos/formulario', FormularioAlunoListView.as_view(), name='formulario_aluno'),
    path('alunos/deletar', DeletarAlunoListView.as_view(), name='deletar_aluno'),
    # Página de Professores
    path('professores/list', ProfessorListView.as_view(), name='listar_professores'),
    path('professores/detalhe', DetalheProfessorListView.as_view(), name='detalhe_professor'),
    path('professores/formulario', FormularioProfessorListView.as_view(), name='formulario_professor'),
    path('professores/deletar', DeletarProfessorListView.as_view(), name='deletar_professor'),  
]

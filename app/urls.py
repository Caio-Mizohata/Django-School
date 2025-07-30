from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from core.views import HomeListView, HomeLoginView, HomeRegisterView, logout_view
from alunos.views import AlunosListView, DetalheAlunoListView, FormularioAlunoListView, DeletarAlunoListView
from professores.views import ProfessorListView, DetalheProfessorListView, FormularioProfessorListView, DeletarProfessorListView

urlpatterns = [
    path('admin/', admin.site.urls),
    # Página principal
    path('', HomeListView.as_view(), name='home'),
    path('login/', HomeLoginView.as_view(), name='login'),
    path('register/', HomeRegisterView.as_view(), name='register'),
    path('logout/', logout_view, name='logout'),
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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django import forms
from alunos.models import AlunosModel

class AlunoForm(forms.Form):
    nome_aluno = forms.CharField(max_length=100)
    data_nascimento = forms.DateField()
    endereco = forms.CharField(max_length=200)
    telefone = forms.CharField(max_length=20)
    email = forms.EmailField()

    class Meta():
        model = AlunosModel
        fields = '__all__'
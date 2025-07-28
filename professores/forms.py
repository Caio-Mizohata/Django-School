from django import forms
from professores.models import ProfessoresModel

class ProfessorForm(forms.Form):
    nome_professor = forms.CharField(max_length=100)
    data_nascimento = forms.DateField()
    endereco = forms.CharField(max_length=200)
    telefone = forms.CharField(max_length=20)
    email = forms.EmailField()

    class Meta():
        model = ProfessoresModel
        fields = '__all__'
        
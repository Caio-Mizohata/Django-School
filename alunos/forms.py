from django import forms
from alunos.models import AlunosModel, EscolaModel

class AlunoForm(forms.ModelForm):
    class Meta:
        model = AlunosModel
        fields = '__all__'

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if not cpf or not cpf.isdigit() or len(cpf) != 11:
            raise forms.ValidationError('CPF inválido')
        return cpf

    def clean_rg(self):
        rg = self.cleaned_data.get('rg')
        if rg and (not rg.isdigit() or len(rg) != 9):
            raise forms.ValidationError('RG inválido')
        return rg

    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone')
        if telefone and not telefone.isdigit():
            raise forms.ValidationError('Telefone inválido')
        return telefone

    def clean(self):
        cleaned_data = super().clean()
        self.telefone = cleaned_data.get('telefone')
        telefone_responsavel = cleaned_data.get('telefone_responsavel')
        if telefone_responsavel and not telefone_responsavel.isdigit():
            self.add_error('telefone_responsavel', 'Telefone do responsável inválido')
        return cleaned_data


class EscolaForm(forms.ModelForm):
    class Meta:
        model = EscolaModel
        fields = '__all__'

    def clean_turma(self):
        turma = self.cleaned_data.get('turma')
        if not turma or not turma.isalpha():
            raise forms.ValidationError('Turma inválida')
        return turma
    
    def clean_serie(self):
        serie = self.cleaned_data.get('serie')
        if not serie or not serie.isdigit():
            raise forms.ValidationError('Série inválida')
        return serie
    
    def clean_ano(self):
        ano = self.cleaned_data.get('ano')
        if not ano or not ano.isdigit() or len(ano) < 4:
            raise forms.ValidationError('Ano inválido')
        return ano

    def clean_turno(self):
        turno = self.cleaned_data.get('turno')
        if not turno or not turno.isalpha():
            raise forms.ValidationError('Turno inválido')
        return turno

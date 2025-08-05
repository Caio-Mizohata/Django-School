from django import forms
from alunos.models import AlunosModel

class AlunoForm(forms.ModelForm):
    class Meta:
        model = AlunosModel
        fields = '__all__'

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if cpf and (not cpf.isdigit() or len(cpf) != 11):
            raise forms.ValidationError('CPF inválido. Se preenchido, deve conter 11 dígitos.')
        return cpf

    def clean_rg(self):
        rg = self.cleaned_data.get('rg')
        if rg and not rg.isdigit():
            raise forms.ValidationError('RG inválido. Forneça apenas os números.')
        return rg

    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone')
        if telefone and not telefone.isdigit():
            raise forms.ValidationError('Telefone inválido')
        return telefone

    def clean(self):
        cleaned_data = super().clean()
        telefone_responsavel = cleaned_data.get('telefone_responsavel')
        telefone_pai = cleaned_data.get('telefone_pai')
        telefone_mae = cleaned_data.get('telefone_mae')

        if not telefone_responsavel and not telefone_pai and not telefone_mae:
            raise forms.ValidationError("É obrigatório informar o telefone de contato de pelo menos um responsável (pai, mãe ou outro).", code='no_responsible_phone')

        if cleaned_data.get('pai_responsavel') and not telefone_pai:
            self.add_error('telefone_pai', 'O telefone do pai é obrigatório se o nome for informado.')

        if cleaned_data.get('mae_responsavel') and not telefone_mae:
            self.add_error('telefone_mae', 'O telefone da mãe é obrigatório se o nome for informado.')

        if cleaned_data.get('nome_responsavel') and not telefone_responsavel:
            self.add_error('telefone_responsavel', 'O telefone do responsável é obrigatório se o nome for informado.')

        return cleaned_data

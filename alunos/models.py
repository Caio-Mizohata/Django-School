from django.db import models


class AlunosModel(models.Model):
  
    SEXO = (
        ('MASCULINO', 'Masculino'),
        ('FEMININO', 'Feminino'),
    )

    SERIE_DO_ALUNO = (
        ('1° ANO', '1º Ano'),
        ('2° ANO', '2º Ano'),
        ('3° ANO', '3º Ano'),
        ('4° ANO', '4º Ano'),
        ('5° ANO', '5º Ano'),
        ('6° ANO', '6º Ano'),
        ('7° ANO', '7º Ano'),
        ('8° ANO', '8º Ano'),
        ('9° ANO', '9º Ano'),
        ('1° ANO Ensino Médio', '1º Ano Ensino Médio'),
        ('2° ANO Ensino Médio', '2º Ano Ensino Médio'),
        ('3° ANO Ensino Médio', '3º Ano Ensino Médio'),
    )

    TURNO_DO_ALUNO = (
        ('MANHÃ', 'Manhã'),
        ('TARDE', 'Tarde'),
        ('NOITE', 'Noite'),
    )

    nome_aluno = models.CharField(max_length=100)
    foto_aluno = models.ImageField(upload_to='fotos_alunos/', blank=True, null=True)
    idade = models.IntegerField(blank=False, null=True)
    sexo = models.CharField(max_length=10, choices=SEXO)
    data_nascimento = models.DateField(blank=False, null=True)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    cpf = models.CharField(max_length=11, blank=True, null=True, help_text="Apenas 11 dígitos")
    rg = models.CharField(max_length=20, blank=True, null=True, help_text="Apenas números")
    pai_responsavel = models.CharField(max_length=100, blank=True, null=True)
    telefone_pai = models.CharField(max_length=20, blank=True, null=True, help_text="Apenas números")
    mae_responsavel = models.CharField(max_length=100, blank=True, null=True)
    telefone_mae = models.CharField(max_length=20, blank=True, null=True, help_text="Apenas números")
    nome_responsavel = models.CharField(max_length=100, blank=True, null=True)
    telefone_responsavel = models.CharField(max_length=20, blank=True, null=True, help_text="Apenas números")
    data_matricula = models.DateField(blank=False, null=True)
    serie = models.CharField(max_length=20, choices=SERIE_DO_ALUNO, blank=False, null=True)
    turno = models.CharField(max_length=10, choices=TURNO_DO_ALUNO, blank=False, null=True)

    def __str__(self):
        return self.nome_aluno

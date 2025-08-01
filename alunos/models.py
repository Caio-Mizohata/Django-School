from django.db import models

class AlunosModel(models.Model):
    ESTADO_DO_ALUNO = (
        ('Ativo', 'ATIVO'),
        ('Inativo', 'INATIVO'),
    )

    SEXO = (
        ('Masculino', 'MASCULINO'),
        ('Feminino', 'FEMININO'),
    )

    id = models.AutoField(primary_key=True)
    nome_aluno = models.CharField(max_length=100)
    estado_do_aluno = models.CharField(max_length=10, choices=ESTADO_DO_ALUNO, default='Ativo')
    sexo = models.CharField(max_length=10, choices=SEXO, default=None)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    cpf = models.CharField(max_length=11, blank=True, null=True)
    rg = models.CharField(max_length=20, blank=True, null=True)
    pai_responsavel = models.CharField(max_length=100, blank=True, null=True)
    mae_responsavel = models.CharField(max_length=100, blank=True, null=True)
    nome_responsavel = models.CharField(max_length=100, blank=True, null=True)
    telefone_responsavel = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nome_aluno


class EscolaModel(models.Model):
    aluno = models.ForeignKey(AlunosModel, on_delete=models.PROTECT, related_name='escola')
    turma = models.CharField(max_length=100)
    ano = models.IntegerField(blank=False, null=True)
    serie = models.CharField(max_length=100)
    turno = models.CharField(max_length=100)
    data_matricula = models.DateField()

    def __str__(self):
        return f"{self.turma} - {self.serie} ({self.aluno.nome_aluno})"

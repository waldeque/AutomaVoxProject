from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


class GrupoConta(models.Model):
    codigo_grupo = models.IntegerField(unique=True)
    nome_grupo = models.CharField(u'Grupo', max_length=50, unique=True)

    def __unicode__(self):
        return u'%s' % (self.codigo_grupo)

    def retornar_cod_nome(self):
        return u'%s %s' % (self.codigo_grupo, self.nome_grupo)


class Condominio(models.Model):
    codigo_condominio = models.IntegerField(unique=True)
    nome_condominio = models.CharField(max_length=50)
    logradouro = models.CharField(u'Logradouro', max_length=100)
    numero = models.IntegerField()
    bairro = models.CharField(u'Bairro', max_length=50)
    cep = models.CharField('CEP', max_length=8)
    complemento = models.CharField(max_length=200, null=True, blank=True)
    cidade = models.CharField(u'Cidade', max_length=50)
    estado = models.CharField(u'UF', max_length=2)

    def __str__(self):
        return self.codigo_condominio

    def retornar_cod_nome(self):
        return u'%s %s' % (self.codigo_condominio, self.nome_condominio)


class Inquilino(models.Model):
    CHOICES_SEXO = (('M', 'Masculino'), ('F', 'Feminino'))
    cpf_inquilino = models.CharField('CPF', max_length=11, unique=True)
    rg_inquilino = models.IntegerField()
    uf = models.CharField(u'UF', max_length=2)
    nome_inquilino = models.CharField(max_length=30)
    sobrenome_inquilino = models.CharField(max_length=30)
    sexo_inquilino = models.CharField(u'Sexo', max_length=1, choices=CHOICES_SEXO)
    nascimento = models.DateField(u'Data de nascimento')

    def __str__(self):
        return self.cpf_inquilino

    def retornar_nome_sobrenome(self):
        return u'%s %s' % (self.nome_inquilino, self.sobrenome_inquilino)

class Conta(models.Model):
    grupoContas = models.CharField(max_length=60)#models.ForeignKey(GrupoConta.retornar_cod_nome())
    codigo_conta = models.IntegerField(unique=True)
    condominio = models.CharField(max_length=60)#models.ForeignKey(Condominio.retornar_cod_nome())
    cpf_inquilino = models.CharField('CPF', max_length=11, unique=True)
    nome_inquilino = models.CharField(max_length=60)
    valor = models.DecimalField(max_digits=10, decimal_places=2, blank=False, default=0)
    vencimento = models.DateTimeField(blank=False)

    def __str__(self):
        return self.codigo_conta

from django.contrib.auth.models import User
from django.db import models

from utils.lista_municipios import lista_municipio, lista_municipio_amb


class Transferencias_Ped(models.Model):
    date_reg_transf = models.DateTimeField(blank=True, default='',null=True)
    date_transf = models.DateTimeField()
    pac = models.CharField(max_length=50)
    data_nasc = models.DateField()
    mtv_dgt = models.TextField()
    dest = models.CharField(max_length=5)
    munic = models.CharField(choices=lista_municipio, max_length=50)
    espec = models.CharField(max_length=50)
    scd = models.IntegerField()
    ch_y_n = (
        ('S', 'Sim'),
        ('N', 'Não'),
    )
    ch_amb = (
        ('S','UTI'),
        ('N','BÁSICA')
    )
    acomp = models.CharField(choices=ch_y_n, max_length=10)
    ambul = models.CharField(choices=ch_amb, max_length=20)
    local_ambul = models.CharField(choices=lista_municipio_amb, max_length=50)
    contref = models.CharField(blank=True, default='',null=True,max_length=50)
    obs = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )
    author_reg = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.pac

class Transferencias_Adu(models.Model):
    date_reg_transf = models.DateTimeField(blank=True, default='',null=True)
    date_transf = models.DateTimeField()
    pac = models.CharField(max_length=50)
    data_nasc = models.DateField()
    mtv_dgt = models.TextField()
    dest = models.CharField(max_length=5)
    munic = models.CharField(choices=lista_municipio, max_length=50)
    espec = models.CharField(max_length=50)
    scd = models.IntegerField()
    ch_y_n = (
        ('S', 'Sim'),
        ('N', 'Não'),
    )
    ch_amb = (
        ('S','UTI'),
        ('N','BÁSICA')
    )
    acomp = models.CharField(choices=ch_y_n, max_length=10)
    ambul = models.CharField(choices=ch_amb, max_length=20)
    local_ambul = models.CharField(choices=lista_municipio_amb, max_length=50)
    contref = models.CharField(blank=True, default='',null=True,max_length=50)
    obs = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )
    author_reg = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.pac

class Transferencias_Ges(models.Model):
    date_reg_transf = models.DateTimeField(blank=True, default='',null=True)
    date_transf = models.DateTimeField()
    pac = models.CharField(max_length=50)
    data_nasc = models.DateField()
    mtv_dgt = models.TextField()
    dest = models.CharField(max_length=5)
    munic = models.CharField(choices=lista_municipio, max_length=50)
    espec = models.CharField(max_length=50)
    scd = models.IntegerField()
    ch_y_n = (
        ('S', 'Sim'),
        ('N', 'Não'),
    )
    ch_amb = (
        ('S','UTI'),
        ('N','BÁSICA')
    )
    acomp = models.CharField(choices=ch_y_n, max_length=10)
    ambul = models.CharField(choices=ch_amb, max_length=20)
    local_ambul = models.CharField(choices=lista_municipio_amb, max_length=50)
    contref = models.CharField(blank=True, default='',null=True,max_length=50)
    obs = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )
    author_reg = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.pac
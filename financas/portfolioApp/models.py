from django.db import models
from django.contrib.auth.models import User


class Carteira(models.Model):
    
    STATUS_CHOICE =(
        ("comprar","comprar"),
        ("vender","vender"),
        ("aguardar","aguardar")
    )
    
    TIPO_CHOICES =(
        ('acao','acao'),
        ('bdr','bdr'),
        ('fii','fii'),
        ('renda fixa','renda fixa'),
    )

    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user', default='')
    ativo = models.CharField(max_length=255)
    quantidade = models.FloatField()
    cotacao = models.FloatField(blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)
    
    meta = models.FloatField(default=0)
    
    tipo = models.CharField(max_length=255,choices=TIPO_CHOICES)
    status = models.CharField(max_length=255,choices=STATUS_CHOICE)
    comentarios = models.TextField(default='',blank=True, null=True)

    class Meta:
        unique_together = ('user', 'ativo',)


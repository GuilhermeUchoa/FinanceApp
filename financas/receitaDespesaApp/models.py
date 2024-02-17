from django.db import models
from django.contrib.auth.models import User

class ReceitaDespesas(models.Model):
    """Receitas e despesas"""

    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='userRD', default='')
    data = models.DateField(blank=True, null=True)
    conta = models.CharField(max_length=255, blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)
    classificacao = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        unique_together = ('conta', 'data','user')


class PadraoDeConta(models.Model):
    """Contas padronizadas"""

    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='userPC', default='')
    contaPadrao = models.CharField(max_length=255, blank=True, null=True)
    vencimento = models.CharField(max_length=5,blank=True, null=True)

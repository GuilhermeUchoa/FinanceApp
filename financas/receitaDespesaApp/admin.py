from django.contrib import admin
from . models import ReceitaDespesas, PadraoDeConta

@admin.register(ReceitaDespesas)
class ReceitaDespesasAdmin(admin.ModelAdmin):
    list_display = ['user','conta','classificacao','status']
    

@admin.register(PadraoDeConta)
class PadraoDeContaAdmin(admin.ModelAdmin):
    list_display = ['contaPadrao','vencimento']
    


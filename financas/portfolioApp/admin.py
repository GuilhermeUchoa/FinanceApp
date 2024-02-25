from django.contrib import admin
from . models import Carteira

@admin.register(Carteira)
class CarteiraAdmin(admin.ModelAdmin):
    list_display = ['user','ativo','cotacao','quantidade','valor','meta','tipo','status','comentarios']
    list_editable = ['meta']
    
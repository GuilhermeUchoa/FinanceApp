from django.urls import path
from . import views

app_name='receitaDespesaApp'

urlpatterns = [
    path('',views.receitaDespesa, name='receitaDespesa'),
    path('receitaDespesa_post/',views.receitaDespesa_post, name='receitaDespesa_post'),
    path('addInfomation/',views.addInfomation, name='addInfomation'),
    path('addContaPadrao/',views.addContaPadrao, name='addContaPadrao'),
    path('refreshInfomation/<int:id>/',views.refreshInfomation, name='refreshInfomation'),
    path('excluir/<int:id>/',views.excluir, name='excluir'),

]
from django.urls import path
from . import views

app_name = 'portfolioApp'

urlpatterns = [
    path('',views.portfolio, name='portfolio'),
    path('addAtivo/',views.addAtivo, name='addAtivo'),
    path('delAtivo/<int:id>/',views.delAtivo, name='delAtivo'),
    path('addCei/',views.addCei, name='addCei'),
    path('atualizarCotacao/',views.atualizarCotacao, name='atualizarCotacao'),
    path('atualizarMeta/<int:id>/',views.atualizarMeta, name='atualizarMeta'),
    path('atualizarComentario/<int:id>/',views.atualizarComentario, name='atualizarComentario'),
    path('atualizarStatus/<int:id>/',views.atualizarStatus, name='atualizarStatus'),
]
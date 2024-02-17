from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from . carteiraAddCei import carteiraAddCei
from . forms import adicionarAtivoForms
from django.db.models import Sum
from . models import Carteira
import yfinance as yf
import pandas as pd
import warnings
warnings.simplefilter("ignore")

@login_required
def portfolio(request):
    
    context = {
        #Formulario para adicionar ativos manualmente
        'adicionarAtivoForms' : adicionarAtivoForms,
        
        #Retorna os ativos separados por tipo
        'carteira' : Carteira.objects.filter(user_id = request.user.id).order_by('tipo'),  #Aqui consigo definir a prioridade e apresentar qual comprar primeiro
        'valorTotal' : Carteira.objects.filter(user_id = request.user.id).aggregate(Sum('valor'))['valor__sum'],
        'acaoValor' : Carteira.objects.filter(user_id = request.user.id, tipo = 'acao').aggregate(Sum('valor'))['valor__sum'],
        'bdrValor' : Carteira.objects.filter(user_id = request.user.id, tipo = 'bdr').aggregate(Sum('valor'))['valor__sum'],
        'fiiValor' : Carteira.objects.filter(user_id = request.user.id, tipo = 'fii').aggregate(Sum('valor'))['valor__sum'],

        
    }   

    return render(request,'portfolio/portfolio.html',context=context)

@login_required
def addAtivo(request):
    """Adiciona ativo manualmente"""
    if request.method == 'POST':
        
        carteira = Carteira(
            user_id = request.user.id,
            ativo = request.POST['ativo'].upper(),
            quantidade = request.POST['quantidade'] or 0,
            cotacao = request.POST['cotacao'] or 0,
            valor = request.POST['valor'] or 0,
            tipo = request.POST['tipo'],
        )
        carteira.save()

    return redirect('portfolioApp:portfolio')

@login_required
def delAtivo(request,id):
    """Deleta ativos"""
    get_object_or_404(Carteira, id=id).delete()
    
    return redirect('portfolioApp:portfolio')

@login_required
def addCei(request):
    """Adiciona a carteira baixada de CEI em formato excel"""
    carteiraAddCei(request,request.FILES['file'])
    
    atualizarCotacao(request)

    return redirect('portfolioApp:portfolio')


@login_required
def atualizarCotacao(request):
    """Atualiza as cotacoes"""
    df = pd.DataFrame(round(yf.download([i.ativo+'.SA' for i in Carteira.objects.filter(user_id = request.user.id).exclude(tipo='RENDA FIXA')],
                                        start='2024-01-02',
                                        end='2024-02-16',
                                        threads=True)['Close'],2))
    df.fillna(0,inplace=True)

    for i in df:
        
        ativo = str(i[:-3])
        cotacao = df[i][-1]
        carteira = get_object_or_404(Carteira,ativo=ativo,user_id = request.user.id)
        carteira.cotacao = cotacao
        carteira.valor = cotacao * carteira.quantidade
        carteira.save()

    return redirect('portfolioApp:portfolio')


@login_required
def atualizarMeta(request,id):
    """Adicionar o valor de meta"""
    if request.method == 'POST':
        carteira = get_object_or_404(Carteira, id=id, user_id = request.user.id)
        carteira.meta = request.POST['meta']
        carteira.save()
        

    return redirect('portfolioApp:portfolio')



def atualizarComentario(request,id):

    if request.method == 'POST':

        carteira = get_object_or_404(Carteira,id=id,user_id = request.user.id)
        carteira.comentarios = request.POST['textoComentario']
        carteira.save()

    return redirect('portfolioApp:portfolio')


@login_required
def atualizarStatus(request,id):
    """Atualizar status"""
    carteira = get_object_or_404(Carteira,id=id,user_id = request.user.id)
    carteira.status = request.GET["status"]
    carteira.save()

    return redirect('portfolioApp:portfolio')
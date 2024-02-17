from django.shortcuts import render, redirect
from . models import ReceitaDespesas, PadraoDeConta
from django.shortcuts import get_object_or_404
from . forms import AddContasForms
from django.db.models import Sum
import datetime
from django.contrib.auth.decorators import login_required

@login_required
def receitaDespesa(request):

    if request.method == 'GET':
        ano = str(int(datetime.date.isoformat(datetime.datetime.today())[:4]))
        mes = str(int(datetime.date.isoformat(datetime.datetime.today())[5:7]))
    
    receita = ReceitaDespesas.objects.filter(user_id = request.user.id, classificacao='RECEITA',data__year=ano, data__month=mes).aggregate(Sum('valor'))['valor__sum']
    despesa = ReceitaDespesas.objects.filter(user_id = request.user.id, classificacao='DESPESA',data__year=ano, data__month=mes).aggregate(Sum('valor'))['valor__sum'] 

    if receita == None:
        receita = 0
    if despesa == None:
        despesa = 0

    saldo = float(receita) - float(despesa)

    context = {
        'ReceitaDespesas':ReceitaDespesas.objects.filter(user_id = request.user.id, data__year=ano, data__month=mes).order_by('-classificacao'),
        'PadraoDeConta':PadraoDeConta.objects.filter(user_id = request.user.id),
        'AddContasForms': AddContasForms,
        'saldo':saldo,
    }
    
    return render(request, 'receitaDespesa/receitaDespesa.html',context=context)

@login_required
def receitaDespesa_post(request):
    print('Ola mundo')
    #Post com data
    if request.method == 'POST':
        ano = str(request.POST['data'][:4])
        mes = str(int(request.POST['data'][5:]))
    
    receita = ReceitaDespesas.objects.filter(user_id = request.user.id, classificacao='RECEITA',data__year=ano, data__month=mes).aggregate(Sum('valor'))['valor__sum']
    despesa = ReceitaDespesas.objects.filter(user_id = request.user.id, classificacao='DESPESA',data__year=ano, data__month=mes).aggregate(Sum('valor'))['valor__sum'] 

    if receita == None:
        receita = 0
    if despesa == None:
        despesa = 0

    saldo = float(receita) - float(despesa)

    context = {
        'ReceitaDespesas':ReceitaDespesas.objects.filter(user_id = request.user.id, data__year=ano, data__month=mes).order_by('-classificacao'),
        'AddContasForms': AddContasForms,
        'saldo':saldo,
    }
    
    return render(request, 'receitaDespesa/componentes/tableModel.html',context=context)

@login_required
def addInfomation(request):
    if request.method == 'POST':
        data = ReceitaDespesas(
            user_id = request.user.id,
            data = request.POST['data'],
            conta = request.POST['conta'].upper(),
            valor = request.POST['valor'],
            classificacao = request.POST['classificacao'],
            status = request.POST['status'],
        )
        data.save()

    return redirect('receitaDespesaApp:receitaDespesa')

@login_required
def refreshInfomation(request,id):

    if request.method == 'POST':
        print(request.POST)
        
        data = get_object_or_404(ReceitaDespesas,id=id)

        try:
            data.conta = request.POST['conta'].upper()
        except:
            pass
        try:
            data.valor = request.POST['valor']
        except:
            pass
        try:
            data.classificacao = request.POST['classificacao']
        except:
            pass
        try:
            data.status = request.POST['status']
        except:
            pass
        
        data.save()

    return redirect('receitaDespesaApp:receitaDespesa_post')

@login_required
def excluir(request,id):

    if request.method == 'POST':

        get_object_or_404(ReceitaDespesas,id=id).delete()
        
    return redirect('receitaDespesaApp:receitaDespesa')

@login_required
def addContaPadrao(request):
    
    if request.method == 'POST':

        data = ReceitaDespesas(
            user_id = request.user.id,
            data = datetime.datetime.today().date(),
            conta = request.POST['conta'].upper(),
            valor = 0,
            classificacao = '',
            status = '',
        )
        data.save()
  

    return redirect('receitaDespesaApp:receitaDespesa')
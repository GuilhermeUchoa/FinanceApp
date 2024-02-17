from . models import Carteira
import pandas as pd

#Preciso melhorar esse codigo

def carteiraAddCei(request, arquivo):

    df_acoes = pd.read_excel(arquivo,sheet_name=0).dropna()
    df_bdr = pd.read_excel(arquivo,sheet_name=1).dropna()
    df_fii = pd.read_excel(arquivo,sheet_name=2).dropna()  

    dictAtivo = {'acao':df_acoes,
                 'bdr':df_bdr,
                 'fii':df_fii,
                 }
    
    for chave,valor in dictAtivo.items():
        
        for i in range(len(valor)):
        
            ativo = valor['Código de Negociação'].loc[i]
            quantidade = int(valor['Quantidade'].loc[i])
     
            try:
                Carteira.objects.filter(ativo=ativo, user_id = request.user.id).get()
                if Carteira.objects.filter(ativo=ativo,user_id = request.user.id).get().ativo == ativo:
                    carteira = Carteira.objects.filter(ativo=ativo,user_id = request.user.id).get()
                    carteira.quantidade = quantidade
                    carteira.save()
                    print(f'Ativo {ativo} atualizado')
            except:
                carteira = Carteira(
                    user_id = request.user.id,
                    ativo = ativo,
                    quantidade = quantidade,
                    cotacao = 0,
                    valor = 0,
                    tipo = chave
                    )
                carteira.save()
                print(f'novo ativo {ativo} adicionado a carteira')
                
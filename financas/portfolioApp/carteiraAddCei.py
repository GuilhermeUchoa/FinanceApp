from . models import Carteira
import pandas as pd

#Preciso melhorar esse codigo

def carteiraAddCei(request, arquivo):

    df_acoes = pd.read_excel(arquivo,sheet_name=0).dropna()
    df_bdr = pd.read_excel(arquivo,sheet_name=1).dropna()
    df_fii = pd.read_excel(arquivo,sheet_name=2).dropna() 
    df_rf = pd.read_excel(arquivo,sheet_name=3).dropna()  

    dictAtivo = {'acao':df_acoes,
                 'bdr':df_bdr,
                 'fii':df_fii,
                 'renda fixa':df_rf,
                 }
    
    for chave,valor in dictAtivo.items():
        
        for i in range(len(valor)):

            if chave == 'renda fixa':
                ativo = valor['Produto'].loc[i]
                quantidade = int(valor['Valor líquido'].loc[i])
                valor = int(valor['Valor líquido'].loc[i])
                cotacao = 1

            else:
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
            
                if chave == 'renda fixa':
                    carteira = Carteira(
                        user_id = request.user.id,
                        ativo = ativo,
                        quantidade = quantidade,
                        cotacao = cotacao,
                        valor = valor,
                        tipo = chave
                        )
                else:
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
                
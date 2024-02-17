from django import forms

class adicionarAtivoForms(forms.Form):

    TIPO_CHOICES =(
        ('ACAO','ACAO'),
        ('BDR','BDR'),
        ('FII','FII'),
        ('RENDA FIXA','RENDA FIXA'),
    )
    classeCSS = 'input input-bordered input-sm w-full max-w-xs'
    
    ativo = forms.CharField(max_length=255)
    quantidade = forms.IntegerField()
    cotacao = forms.FloatField(required=False)
    valor = forms.FloatField(required=False)
    tipo = forms.ChoiceField(choices=TIPO_CHOICES,required=True)

    ativo.widget.attrs.update({'class':classeCSS,'placeholder':'ativo'} )
    quantidade.widget.attrs.update({'class':classeCSS,'placeholder':'quantidade'} )
    cotacao.widget.attrs.update({'class':classeCSS,'placeholder':'cotacao'} )
    valor.widget.attrs.update({'class':classeCSS,'placeholder':'valor'} )
    tipo.widget.attrs.update({'class':classeCSS,'placeholder':'tipo'} )

    


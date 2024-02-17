from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'
class AddContasForms(forms.Form):

    CLASSIFICACAO_CHOICE= (
        ('RECEITA','RECEITA'),
        ('DESPESA','DESPESA'),
    )

    STATUS_CHOICE =(
        ('PAGO','PAGO'),
        ('INADIPLENTE','INADIPLENTE'),
    )
    
    classeCSS = 'input input-bordered w-full max-w-xs receitadespesaForm'
    
    data = forms.DateField(widget=DateInput)
    conta = forms.CharField(max_length=255)
    valor = forms.FloatField()
    classificacao = forms.ChoiceField(choices=CLASSIFICACAO_CHOICE)
    status = forms.ChoiceField(choices=STATUS_CHOICE)


    conta.widget.attrs.update({'class':classeCSS,'placeholder':'conta'} )
    valor.widget.attrs.update({'class':classeCSS,'placeholder':'valor'} )
    classificacao.widget.attrs.update({'class':classeCSS,'placeholder':'classificacao'} )
    status.widget.attrs.update({'class':classeCSS,'placeholder':'status'} )
    data.widget.attrs.update({'class':classeCSS,'placeholder':'status'} )
    





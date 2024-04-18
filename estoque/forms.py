from django import forms
from .models import Estoque, Categoria

class EstoqueForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), empty_label="Escolha a Categoria")
    
    class Meta:
        model = Estoque
        fields = ('produto', 'quantidade_em_estoque', 'categoria', 'imagem')

class FiltroProdutoForm(forms.Form):
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), required=False, label="Categoria")
#class EstoqueForm(forms.ModelForm):
#
    #class Meta:
        #model = Estoque
        #fields = ('produto', 'quantidade_em_estoque', 'imagem')

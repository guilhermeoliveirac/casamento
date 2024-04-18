from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import F
from django.urls import reverse
from .models import Estoque, Categoria
from .forms import EstoqueForm, FiltroProdutoForm

def index(request):
    produtos = Estoque.objects.all()
    categorias = Categoria.objects.all()  # Adicionando todas as categorias disponíveis
    return render(request, 'estoque/index.html', {'produtos': produtos, 'categorias': categorias})
    

def adicionar_produto(request):
    if request.method == 'POST':
        form = EstoqueForm(request.POST, request.FILES)  # Incluir request.FILES é crucial para o upload de arquivos
        if form.is_valid():
            form.save()
            messages.success(request, 'adicionado com sucesso!')
            return redirect('index')
    else:
        form = EstoqueForm()
    return render(request, 'estoque/form_produto.html', {'form': form})

def remover_produto(request, pk):
    produto_para_remover = Estoque.objects.get(pk=pk)
    produto_para_remover.delete()
    messages.success(request, f'O Produto {produto_para_remover.produto} foi removido com sucesso!')
    return redirect('index')

def modificar_produto(request, pk):
    produto_para_modificar = Estoque.objects.get(pk=pk)
    if request.method == 'POST':
        form = EstoqueForm(request.POST, instance=produto_para_modificar)
        if form.is_valid():
            produto_para_modificar = form.save(commit=False)
            produto_para_modificar.produto = form.data['produto']
            produto_para_modificar.quantidade_em_estoque = form.data['quantidade_em_estoque']
            #produto_para_modificar.estoque_minimo = form.data['estoque_minimo']
            produto_para_modificar.save()
            messages.success(request, f'O produto {produto_para_modificar.produto} foi alterado com sucesso!')
            return redirect('index')
    else:
        form = EstoqueForm(instance=produto_para_modificar)
    return render(request, 'estoque/form_produto.html', {'form': form})
    return redirect('index')
    return render(request, 'estoque/index.html', {'produtos': produtos_em_falta, 'form': form})

def produtos_em_falta(request):
    categoria_id = request.GET.get('categoria')
    if categoria_id:
        # Filtra os produtos em falta baseando-se na categoria
        produtos_em_falta = Estoque.objects.filter(quantidade_em_estoque=0, categoria_id=categoria_id)
    else:
        # Se não houver categoria especificada, mostra todos os produtos em falta
        produtos_em_falta = Estoque.objects.filter(quantidade_em_estoque=0)
    categorias = Categoria.objects.all()
   
    return render(request, 'estoque/produtos_em_falta.html', {
        'produtos_em_falta': produtos_em_falta,
        'categorias': categorias
    })

def produtos_existentes(request):
    categoria_id = request.GET.get('categoria')
    if categoria_id:
        # Filtra os produtos em falta baseando-se na categoria
        produtos_existentes = Estoque.objects.filter(quantidade_em_estoque__gt=0, categoria_id=categoria_id)
    else:
        # Se não houver categoria especificada, mostra todos os produtos em falta
        produtos_existentes = Estoque.objects.filter(quantidade_em_estoque__gt=0)
    categorias = Categoria.objects.all()
    print("Produtos em falta:", produtos_existentes.count())
    return render(request, 'estoque/produtos_existentes.html', {
        'produtos_existentes': produtos_existentes,
        'categorias': categorias
    })
   


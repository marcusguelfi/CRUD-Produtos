from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from ..models import Produto
from ..forms import ProdutoForm


def _produtos_filtrados(q):
    return Produto.objects.filter(nome__icontains=q) if q else Produto.objects.all()  


@login_required(login_url='login')
def home(request):
    query = request.GET.get('q', '')
    produtos = _produtos_filtrados(query)
    return render(request, 'home.html', {'produtos': produtos, 'query': query})


@login_required(login_url='login')
def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.usuario = request.user
            produto.save()
            messages.success(request, 'Produto adicionado com sucesso!')
            return redirect('home')  
    else:
        form = ProdutoForm()
    return render(request, 'adicionar_produto.html', {'form': form})


@login_required(login_url='login')
def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)

    if request.method == 'POST' and request.user.has_perm('produtos.change_produto'):
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto atualizado com sucesso!')
            return redirect('home') 
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'editar_produto.html', {'form': form})


@login_required(login_url='login')
def excluir_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    
    if request.user.has_perm('produtos.delete_produto') or request.user.groups.filter(name='Supervisor').exists():
        produto.delete()
        messages.success(request, 'Produto excluído com sucesso!')
    else:
        messages.error(request, 'Você não tem permissão para excluir produtos.')
    
    return redirect('home')  


@login_required(login_url='login')
def buscar_produtos(request):
    produtos_list = list(
        _produtos_filtrados(request.GET.get('q', '')).values("nome", "descricao", "preco", "quantidade")
    )
    return JsonResponse(produtos_list, safe=False)

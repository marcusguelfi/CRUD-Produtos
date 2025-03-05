from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from ..models import Produto
from ..forms import ProdutoForm

@login_required(login_url='login')
def home(request):
    query = request.GET.get('q', '')
    if query:
        produtos = Produto.objects.filter(nome__icontains=query)
    else:
        produtos = Produto.objects.all()
    
    return render(request, 'home.html', {'produtos': produtos, 'query': query})


@login_required(login_url='login')
def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.usuario = request.user
            produto.save()
            return redirect('home')
    else:
        form = ProdutoForm()
    return render(request, 'adicionar_produto.html', {'form': form})

@login_required(login_url='login')
def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'editar_produto.html', {'form': form})

@login_required(login_url='login')
def excluir_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.user.has_perm('produtos.delete_produto') or request.user.groups.filter(name='Supervisor').exists():
        produto.delete()
    return redirect('home')

@login_required(login_url='login')
def buscar_produtos(request):
    query = request.GET.get('q', '')
    produtos = Produto.objects.filter(nome__icontains=query) if query else Produto.objects.all()  
    produtos_json = list(produtos.values("nome", "descricao", "preco", "quantidade"))
    return JsonResponse(produtos_json, safe=False)  


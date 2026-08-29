from django.shortcuts import render, get_object_or_404
from .models import Produto

def lista(request):
    produtos = Produto.objects.all() #select * from produto
    print(produtos)
    return render(request,'lista.html',{ 'produtos':produtos})


def novo(request):
    if request.method == 'POST':
       descricao = request.POST.get('descricao') 
       preco = request.POST.get('preco')
       estoque = request.POST.get('estoque')

       Produto.objects.create(descricao=descricao,preco=preco,estoque=estoque)
       #insert into produtos_produto(descricao,preco,estoque)values('',1,1)
       return lista(request)

    return render(request,'form.html')

def excluir(request,id):
    produto = get_object_or_404(Produto, id=id)
    #select * from Produtos_produto where id = 1
    produto.delete()
    return lista(request)

def editar(request,id):
    produto = get_object_or_404(Produto, id=id)
    
    if request.method == 'POST':
        produto.descricao = request.POST.get('descricao') 
        produto.preco = request.POST.get('preco')
        produto.estoque = request.POST.get('estoque')

        produto.save() #update produtos_produto set         

        return lista(request)
    
    return render(request,'form.html', {'produto':produto})
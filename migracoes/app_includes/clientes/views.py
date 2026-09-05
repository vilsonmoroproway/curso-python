from django.shortcuts import render

from clientes.models import Cliente

def listar(request):
    return render(request, 'clientes/lista.html')

def novo(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')

        Cliente.objects.create(nome=nome,email=email,telefone=telefone)
        return listar(request)
    
    return render(request, 'clientes/novo.html')

def index(request):
    return render(request, 'clientes/index.html')

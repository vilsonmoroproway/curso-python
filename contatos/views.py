from django.shortcuts import render
#from django.http import HttpResponse

def home(request):
    return render(request,'home.html')

def cadastro(request):
    if request.method == 'POST':
       nome = request.POST.get('nome')
       email = request.POST.get('email')
       return consulta(request)
       #return render(request,'consulta.html')

    return render(request,'cadastro.html')


def consulta(request):
    #return HttpResponse('consulta')
    print('consulta')
    return render(request,'consulta.html')

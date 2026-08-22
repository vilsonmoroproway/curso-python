from django.shortcuts import render
from django.http import HttpResponse

def cadastro(request):
    return HttpResponse('cadastro')

def consulta(request):
    return HttpResponse('consulta')

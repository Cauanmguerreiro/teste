from django.shortcuts import render
from django.http import JsonResponse
from .models import Item

def home(request):
    return JsonResponse({"message": "Welcome to the Django backend!"})

def about(request):
    return JsonResponse({"message": "This is the about page."})

def listar_itens(request):
    itens = Item.objects.filter(disponivel=True)
    data = [
        {
            'id': item.id,
            'tipo': item.tipo,
            'descricao': item.descricao,
            'quantidade': item.quantidade,
            'estado_conservacao': item.estado_conservacao,
            'local_retirada': item.local_retirada,
            'contato_doador': item.contato_doador,
        }
        for item in itens
    ]
    return JsonResponse(data, safe=False)
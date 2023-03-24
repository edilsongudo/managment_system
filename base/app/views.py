from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import JsonResponse
import requests
from requests.auth import HTTPBasicAuth
import pprint


@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
@login_required

def create(request):
    api = "http://127.0.0.1:8001/core/"
    
    if request.method == "POST":
       
        image = request.FILES.get('image')
        DNP = request.POST.get('DNP')
        altura = request.POST.get('altura')
        # ponte = request.POST.get('ponte')
        olho_direito = request.POST.get('olho_direito')
        olho_esquerdo = request.POST.get('olho_esquerdo')
        OS = request.POST.get('OS')
        cnpj_otica = request.POST.get('cnpj_otica')
        cnpj_laboratorio = request.POST.get('cnpj_laboratorio')
    
        medicao ={
            'DNP':DNP,
            'altura':altura,
            'olho_direito':olho_direito,
            'olho_esquerdo':olho_esquerdo,
            'OS':OS,
            'cnpj_otica':cnpj_otica,
            'cnpj_laboratorio':cnpj_laboratorio,
        }
        
        files = {'image': (image.name, image.read(), image.content_type)}

        r = requests.post(api,data=medicao,auth=HTTPBasicAuth('administrador', '123456'), files=files)

        return render(request, 'app/obras.html')

        
    if request.method == "GET":
            requisicao = requests.get(api)

            try:
                lista = requisicao.json()
            except ValueError:
                print("A resposta não chegou com o formato esperado.")

            dicionario = {}
            for indice, valor in enumerate(lista):
                dicionario[indice] = valor

            contexto = {
                "medicoes": dicionario
            }

            pp = pprint.PrettyPrinter(indent=4)
            pp.pprint(contexto)

            return render(request, 'app/obras.html',contexto)
        

    

@login_required
def documentacao_1(request):
    api = "http://127.0.0.1:8001//core/"
    requisicao = requests.get(api)
    print(requisicao)

    try:
        lista = requisicao.json()
    except ValueError:
        print("A resposta não chegou com o formato esperado.")

    dicionario = {}
    for indice, valor in enumerate(lista):
        dicionario[indice] = valor

    contexto = {
        "medicoes": dicionario
    }
    return render(request, 'app/documentacao_1.html',contexto)

@login_required
def documentacao_2(request):
    return render(request, 'app/documentacao_2.html')

@login_required
def documentacao_3(request):
    return render(request, 'app/documentacao_3.html')

@login_required
def documentacao_categorias(request):
    return render(request, 'app/documentacao_categorias.html')

@login_required
def upload(request):
    return render(request, 'app/upload.html')
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def obras(request):
    return render(request, 'app/obras.html')

@login_required
def documentacao_1(request):
    return render(request, 'app/documentacao_1.html')

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
from django.http import JsonResponse, HttpResponse

def index(request):
    """
    Página inicial com instruções
    """
    return HttpResponse('''
    <h1>API de Soma</h1>
    <p>Use: /soma/5/8/ para somar dois números</p>
    <p>Exemplo: <a href="/soma/5/8/">/soma/5/8/</a></p>
    ''')

def soma(request, a, b):
    """
    Recebe dois números inteiros e retorna sua soma
    """
    resultado = a + b
    return JsonResponse({'a': a, 'b': b, 'soma': resultado})

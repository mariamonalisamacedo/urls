from django.http import HttpResponse


def boas_vindas(request):
    return HttpResponse("Bem-vindo ao meu site Django!")

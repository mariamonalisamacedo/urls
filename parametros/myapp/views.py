from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def saudacao(request, nome: str) -> HttpResponse:
	"""Retorna uma saudação simples para o nome fornecido."""
	return HttpResponse(f"Olá, {nome}!")

from django.urls import path
from . import views

urlpatterns = [
    path('saudacao/<str:nome>/', views.saudacao, name='saudacao'),
]

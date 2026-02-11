from django.urls import path
import views

urlpatterns = [
    path('', views.index, name='index'),
    path('soma/<int:a>/<int:b>/', views.soma, name='soma'),
]

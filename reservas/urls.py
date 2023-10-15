from django.urls import path
from reservas import views

urlpatterns = [
    path('', views.listar, name='listar'), 
    path('cadastrar/', views.cadastro, name='cadastrar'), 
    path('detalhes/<int:id>/', views.detalhes, name='detalhes'),  
    path('excluir/<int:id>/', views.excluir, name='excluir'),  
    path('atualizar/<int:id>/', views.atualizar, name='atualizar'), 
]

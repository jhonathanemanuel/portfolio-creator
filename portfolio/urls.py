from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('novo_portfolio/', views.novo_portfolio, name='novo_portfolio'),
    path('cadastrar/', views.cadastrar, name='register'),
    path('p/<slug:slug>/', views.detalhe_portifolio, name='visualizar_portfolio'),
    path('editar/<int:pk>/', views.editar_portfolio, name='editar_portfolio'),
    path('dashboard/editar-titulo/<int:pk>/', views.editar_titulo_dashboard, name='editar_titulo_dashboard'),
]

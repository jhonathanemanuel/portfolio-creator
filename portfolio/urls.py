from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('novo_portfolio/', views.novo_portfolio, name='novo_portfolio'),
    path('cadastrar/', views.cadastrar, name='register'),
    path('p/<slug:slug>/', views.detalhe_portifolio, name='visualizar_portfolio'),
]

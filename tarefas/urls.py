from django.urls import path
from . import views

app_name = 'tarefas'

urlpatterns = [
    path('v3/', views.TarefaListCreate.as_view(), name='lista-generic'),
    path('v3/<int:pk>/', views.TarefaDetail.as_view(), name='detalhe-generic'),
]
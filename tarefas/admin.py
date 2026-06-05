from django.contrib import admin
from .models import Tarefa

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    # Colunas exibidas na listagem do admin
    list_display = ['titulo', 'concluida', 'criado_em']
    # Filtro lateral por status de conclusão
    list_filter = ['concluida']
    # Campo de busca para digitar e achar tarefas
    search_fields = ['titulo', 'descricao']
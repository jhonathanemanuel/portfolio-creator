from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Tarefa
from .serializers import TarefaSerializer

class TarefaListCreate(generics.ListCreateAPIView):
    """ GET: Lista apenas tarefas do usuário logado | POST: Cria tarefa vinculada ao usuário """
    serializer_class = TarefaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Tarefa.objects.filter(responsavel=self.request.user)

    def perform_create(self, serializer):
        serializer.save(responsavel=self.request.user)


class TarefaDetail(generics.RetrieveUpdateDestroyAPIView):
    """ GET, PUT, PATCH, DELETE: Gerencia uma tarefa específica se pertencer ao usuário """
    serializer_class = TarefaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Tarefa.objects.filter(responsavel=self.request.user)
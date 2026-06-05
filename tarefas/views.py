from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Tarefa
from .serializers import TarefaSerializer

# =====================================================================
# ─── ESTILO 1: FUNCTION-BASED VIEWS (@api_view) ───
# =====================================================================

@api_view(['GET', 'POST'])
def tarefa_list_create_fbv(request):
    """ GET → Lista todas as tarefas | POST → Cria uma nova tarefa """
    if request.method == 'GET':
        tarefas = Tarefa.objects.all()
        serializer = TarefaSerializer(tarefas, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TarefaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def tarefa_detail_fbv(request, pk):
    """ GET → Detalhe | PUT → Atualiza | DELETE → Exclui uma tarefa """
    try:
        tarefa = Tarefa.objects.get(pk=pk)
    except Tarefa.DoesNotExist:
        return Response({'erro': 'Tarefa nao encontrada'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TarefaSerializer(tarefa)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TarefaSerializer(tarefa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tarefa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# =====================================================================
# ─── ESTILO 2: CLASS-BASED VIEWS (APIView) ───
# =====================================================================

class TarefaListCreateAPIView(APIView):
    """ GET → Lista todas as tarefas | POST → Cria uma nova tarefa """
    def get(self, request):
        tarefas = Tarefa.objects.all()
        serializer = TarefaSerializer(tarefas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TarefaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TarefaDetailAPIView(APIView):
    """ GET → Detalhe | PUT → Atualiza | DELETE → Exclui uma tarefa """
    def get_object(self, pk):
        try:
            return Tarefa.objects.get(pk=pk)
        except Tarefa.DoesNotExist:
            return None

    def get(self, request, pk):
        tarefa = self.get_object(pk)
        if tarefa is None:
            return Response({'erro': 'Tarefa nao encontrada'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TarefaSerializer(tarefa)
        return Response(serializer.data)

    def put(self, request, pk):
        tarefa = self.get_object(pk)
        if tarefa is None:
            return Response({'erro': 'Tarefa nao encontrada'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TarefaSerializer(tarefa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        tarefa = self.get_object(pk)
        if tarefa is None:
            return Response({'erro': 'Tarefa nao encontrada'}, status=status.HTTP_404_NOT_FOUND)
        tarefa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# =====================================================================
# ─── ESTILO 3: GENERIC VIEWS (RECOMENDADO E AUTENTICADO) ───
# =====================================================================

class TarefaListCreate(generics.ListCreateAPIView):
    """ GET → Lista tarefas do usuário logado | POST → Cria tarefa vinculada ao usuário """
    serializer_class = TarefaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Tarefa.objects.filter(responsavel=self.request.user)

    def perform_create(self, serializer):
        serializer.save(responsavel=self.request.user)


class TarefaDetail(generics.RetrieveUpdateDestroyAPIView):
    """ GET/PUT/PATCH/DELETE → Gerencia a tarefa se ela pertencer ao usuário logado """
    serializer_class = TarefaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Tarefa.objects.filter(responsavel=self.request.user)
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from ..models import Produto
from ..serializers import ProdutoSerializer

class ProdutoViewSet(viewsets.ReadOnlyModelViewSet): 
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (SearchFilter,)
    search_fields = ['nome', 'descricao']
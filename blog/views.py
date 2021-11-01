from django.contrib.auth.models import Permission
from django.views.generic import DetailView, ListView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .models import Parceiro
from .models import Xmls
from .models import StatusMaquinas
from rest_framework.response import Response
from .serializer import *
from django_filters  import rest_framework as filters
from rest_framework.decorators import action

class ParceiroFilter(filters.FilterSet):
    class Meta:
        model = Parceiro
        fields = {
            'cnpj': ['icontains'],
            'created': ['iexact', 'lte', 'gte'],
        }

class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class ParceiroListView(ListView):
    model = Parceiro

class ParceiroDetailView(DetailView):
    model = Parceiro

class ParceiroViewSet(viewsets.ModelViewSet):
  #  permission_classes = [IsAuthenticated]
    queryset = Parceiro.objects.all()
    serializer_class = ParceiroSerializer
    filterset_class = ParceiroFilter

    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('created').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)

   # @action(methods=['get'], detail=False)
   # def newest(self, request):
   #     newest = self.get_queryset().order_by('created').last()
    #    serializer = self.get_serializer_class()(newest)
   #     return Response(serializer.data)
 #   permission_classes = [IsAuthenticated]
  #  queryset = Parceiro.objects.all()
#    serializer_class = ParceiroSerializer
 #   filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    #filterset_fields = ['titulo','paginas','editorial__id']
 #   filterset_fields = {
#        'author': ['gte','lte'],
 #       'status': ['contains'],
 #       'cnpj': ['contains']
 #   }
 #   search_fields = ['author', 'status']
 #   ordering_fields = ['pk', 'author']
 #   ordering = ['pk']

    #def get_queryset(self):
    #    queryset =Parceiro.objects.all().select_related('parceiro')
    #    return queryset.filter(paginas__gt=0)

class XmlsListView(ListView):
    model = Xmls

class XmlsDetailView(DetailView):
    model = Xmls

class XmlsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Xmls.objects.all()
    serializer_class = XmlsSerializer

class StatusMaquinasListView(ListView):
    model = StatusMaquinas

class StatusMaquinasDetailView(DetailView):
    model = StatusMaquinas

class StatusMaquinasViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = StatusMaquinas.objects.all()
    serializer_class = StatusMaquinasSerializer
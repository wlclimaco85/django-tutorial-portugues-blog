from django.contrib.auth.models import Permission
from django.views.generic import DetailView, ListView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .models import Parceiro
from .models import Xmls
from .models import StatusMaquinas
from .serializer import *



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
    permission_classes = [IsAuthenticated]
    queryset = Parceiro.objects.all()
    serializer_class = ParceiroSerializer

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
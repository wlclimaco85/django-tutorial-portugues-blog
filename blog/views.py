from django.views.generic import DetailView, ListView
from rest_framework import viewsets
from serializer import PostSerializer
from .models import Post



class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
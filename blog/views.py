from django.views.generic import DetailView, ListView
from rest_framework import viewsets
from .models import Post
from .serializer import PostSerializer



class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
from django.contrib.auth.models import Permission
from django.contrib import admin
from django.views.generic import DetailView, ListView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import User
from rest_framework.response import Response
from .serializer import *
from django_filters  import rest_framework as filters
from rest_framework.decorators import action

class UserFilter(filters.FilterSet):
    class Meta:
        model = User
        fields = {
            'username': ['icontains'],
        }

class UserListView(ListView):
    model = User

class UserDetailView(DetailView):
    model = User

class UserViewSet(viewsets.ModelViewSet):
  #  permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_class = UserFilter

    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('last_login').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)
from django import urls
from django.urls import path
from django.urls.conf import include


from . import views

app_name = "blog"

urlpatterns = [
    path("",views.PostListView.as_view(), name="list"),
    path("<slug:slug>/",views.PostDetailView.as_view(), name="detail"),
    path("<author:author>/",views.ParceiroDetailView.as_view(), name="detail"),

]

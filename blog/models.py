from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ("-created",)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})

class Parceiro(models.Model):
    nome = models.CharField(max_length=255)
    cnpj = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ("-created",)
    def __str__(self):
        return self.nome

class Xmls(models.Model):
    nomeFile = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=255, unique=True)
    xml = models.CharField(max_length=2055)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    parceiro = models.ForeignKey(Parceiro, on_delete=models.CASCADE)
    status = models.CharField(max_length=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ("-created",)
    def __str__(self):
        return self.nome

class StatusMaquinas(models.Model):
    nomeMaquina = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=1)
    dtUltVezOnLine = models.DateTimeField()

    class meta:
        ordering = ("-created",)
    def __str__(self):
        return self.nome

    

    
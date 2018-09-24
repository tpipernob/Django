from django.db import models

class Postagem(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)
    conteudo = models.TextField()

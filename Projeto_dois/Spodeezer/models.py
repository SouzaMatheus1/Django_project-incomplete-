from json import detect_encoding
from django.db import models

# Create your models here.

class Musica(models.Model):
    titulo_musica = models.CharField(max_length=200)
    duracao = models.CharField(max_length=5)
    compositor = models.CharField(max_length=200)
    linkmusica = models.CharField(max_length=200, default="null")
    
    def __str__(self):
        return self.titulo_musica
    
class Album(models.Model):
    titulo_album = models.CharField(max_length=200)
    ano = models.CharField(max_length=4)
    musicas = models.ManyToManyField(Musica)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    capa = models.CharField(max_length=200, default='null')
    
    def __str__(self):
        return self.titulo_album

class Artista(models.Model):
    nome_artista = models.CharField(max_length=200)
    genero = models.CharField(max_length=200)
    ano = models.CharField(max_length=4)
    album = models.ManyToManyField(Album)
    
    def __str__(self):
        return self.nome_artista
    
from inspect import CO_ITERABLE_COROUTINE
from django.shortcuts import render
from django.views import generic

#Models
from .models import Musica, Album, Artista

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'Spodeezer/index.html'
    context_object_name = 'lista_de_artistas'
    
    def get_queryset(self):
        return Artista.objects.all() 

class AlbumView(generic.DetailView):
    model = Artista
    template_name = 'Spodeezer/album.html'


class MusicaView(generic.DetailView):
    model = Album
    template_name = 'Spodeezer/musicas.html'
    
   
class DetalheMusicaView(generic.DetailView):
    model = Musica
    template_name = 'Spodeezer/detalhes.html'
    
    
    
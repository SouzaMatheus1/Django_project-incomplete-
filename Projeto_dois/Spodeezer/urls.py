from django.urls import path 
from . import views 

app_name = 'Spodeezer'
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('album/<int:pk>/',views.AlbumView.as_view(),name='album'),
    path('musica/<int:pk>/',views.MusicaView.as_view(),name='musicas'),
    path('detalhes/<int:pk>/',views.DetalheMusicaView.as_view(),name='detalhesmusica')
]

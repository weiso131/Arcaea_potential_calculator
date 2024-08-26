from django.urls import path
from .views import edit_song_history, edit_song_list

urlpatterns = [
    path('', edit_song_list, name='edit_song_list'),
    path('<str:song_title>/', edit_song_history, name='edit_song_history')
]
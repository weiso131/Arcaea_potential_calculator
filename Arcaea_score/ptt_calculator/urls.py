from django.urls import path
from .views import edit_song_history, edit_song_list, index

urlpatterns = [
    path('', index, name='index'),
    path('edit_song_list/', edit_song_list, name='edit_song_list'),
    path('edit_song_list/<str:song_title>/', edit_song_history, name='edit_song_history')
]
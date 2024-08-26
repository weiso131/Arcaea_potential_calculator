from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Song
from .utils import get_song_history_data


def edit_song_list(request):
    """
    直接重新導向到 edit_song_history
    """
    DEFAULT_CHOICE = Song.objects.first()
    return redirect(reverse('edit_song_history', kwargs={'song_title': DEFAULT_CHOICE}))



def edit_song_history(request, song_title):

    if request.method == "GET":
        choice_song = Song.objects.get(title=song_title)
        song_history = get_song_history_data(choice_song)
        song_list = Song.objects.all()
        
        return render(request, "ptt_calculator/edit_song.html", \
                      {'song_list': song_list, 'choice_song' : choice_song, \
                       'song_history': song_history})
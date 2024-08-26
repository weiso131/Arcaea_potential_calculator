from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Song, Difficulty

def song_list(request):
    song_list = Song.objects.prefetch_related("difficulty_set").all()#prefetch_related 減少查詢次數
    return render(request, "ptt_calculator/song_list.html", {'song_list': song_list})

def edit_song_list(request):
    """
    直接重新導向到 edit_song_history
    """
    DEFAULT_CHOICE = Song.objects.first()
    return redirect(reverse('edit_song_history', kwargs={'song_title': DEFAULT_CHOICE}))



def edit_song_history(request, song_title):

    if request.method == "GET":
        choice_song = Song.objects.get(title=song_title) #之後成用名字找
        choice_song_difficulty = choice_song.difficulty_set
        song_list = Song.objects.all()

        return render(request, "ptt_calculator/edit_song.html", {'song_list': song_list, 'choice_song' : choice_song, 'choice_song_difficulty': choice_song_difficulty})
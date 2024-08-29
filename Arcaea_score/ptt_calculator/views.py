from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Song
from .utils import get_song_history_data, edit_add_record, get_best_30



def index(request):
    user_data = {"user_name" : "teddy", "login" : False, "best_30" : []}
    if request.user.is_authenticated:
        user_data["user_name"] = request.user.username
        user_data["login"] = True
        user_data["best_30"] = get_best_30(request)
    return render(request, 'ptt_calculator/index.html', user_data)


def edit_song_list(request):
    """
    直接重新導向到 edit_song_history
    """
    DEFAULT_CHOICE = Song.objects.first()
    return redirect(reverse('edit_song_history', kwargs={'song_title': DEFAULT_CHOICE}))
   
       


def edit_song_history(request, song_title):
    if not request.user.is_authenticated:
        return render(request, 'ptt_calculator/index.html', {"user_name" : "teddy", "login" : False})
    
    
    
    choice_song = Song.objects.get(title=song_title)
    

    
    if request.method == 'POST':
        edit_add_record(choice_song, request)

    song_history = get_song_history_data(choice_song, request=request)
    song_list = Song.objects.all()
    return render(request, "ptt_calculator/edit_song.html", \
                    {'song_list': song_list, 'choice_song' : choice_song, \
                    'song_history': song_history})
    


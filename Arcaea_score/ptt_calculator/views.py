from django.shortcuts import render
from django.http import HttpResponse
from .models import Song

def song_list(request):
    song_list = Song.objects.prefetch_related("difficulty_set").all()#prefetch_related 減少查詢次數
    return render(request, "ptt_calculator/song_list.html", {'song_list': song_list})



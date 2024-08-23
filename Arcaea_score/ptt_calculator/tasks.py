import time

import logging


from .utils import get_song_data, get_song_list
from .models import Song, Difficulty

logger = logging.getLogger(__name__)


LAST_SONG_DATA = {"level" : ["Past", "Present", "Future", "Moment", "Eternity"],
                  "note" : [680, 781, 831, 888, 790],
                  "chart_constants" : [4.0, 7.0, 9.0, 9.6, 9.7]}


#@background()
# 嘗試做背景處理但失敗了
def crawl_website():
    logger.info('start crawl')
    song_list = get_song_list()
    
    for name, link in song_list:
        if Song.objects.filter(title=name).exists():
            logger.info('Continue')
            continue

        elif name == "Last":
            logger.info('Last')
            last_moment_eternity()
        else:
            add_new_song(name, link)
        
        

# def edit_song(name, link):
#     song_data = get_song_data(link)
#     song = Song.objects.get(title=name)
#     song.img_url = song_data['img']s
#     song.save()

#     for i in range(len(song_data['level'])):
#         difficulty = Difficulty.objects.get(song=song, level=song_data['level'][i])
#         difficulty.note = song_data['note'][i]
#         difficulty.chart_constant = song_data['chart_constants'][i]
#         difficulty.save()

def add_new_song(name, link):
    song_data = get_song_data(link)

    new_song = Song(title=name, img_url=song_data['img'])
    new_song.save()
    for i in range(len(song_data['level'])):
        new_difficulty = Difficulty(level=song_data['level'][i], \
                                    note=song_data['note'][i],
                                    chart_constant=song_data['chart_constants'][i],\
                                    song=new_song)
        new_difficulty.save()
    time.sleep(5)
        
def last_moment_eternity():
    """
    Last Moment:

    終末の地へ降り注ぐ
    今 永遠の摂理塗り替えるヒカリ

    崩れ消えゆく記憶の世界
    ただ一つの譲れない願い

    追い求めたその先に
    たとえ何を失うとしても
    どんな運命も この手で砕いていく
    また出会うため

    誓いをただ ただ繰り返す
    強い意志を力に換えて
    星の道さえ違えてみせるから

    その美しい瞳
    もう傷つけるものはない
    記憶も闇も
    君の心苛む全て
    さあ泣かないで
    怯えずこの手を取って
    ここから ふたり
    """
    last = Song(title="Last", img_url="https://arcwiki.mcd.blue/images/thumb/a/a2/Songs_last.jpg/384px-Songs_last.jpg")
    last.save()
    for i in range(5):
        new_difficulty = Difficulty(level=LAST_SONG_DATA['level'][i], \
                                    note=LAST_SONG_DATA['note'][i],
                                    chart_constant=LAST_SONG_DATA['chart_constants'][i],\
                                    song=last)
        new_difficulty.save()

#TODO: LAST特判, 已經在資料庫的歌不要save，要先找到她再修改
        

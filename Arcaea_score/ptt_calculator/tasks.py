import time

import logging


from .utils import get_song_data, get_song_list
from .models import Song, Difficulty

logger = logging.getLogger(__name__)

#@background()
# 嘗試做背景處理但失敗了
def crawl_website():
    logger.info('start crawl')
    song_list = get_song_list()
    for name, link in song_list:
        
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
        

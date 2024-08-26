from .models import Song

def get_song_history_data(song : Song):
    song_difficulty = song.difficulty_set.all()
    song_history = []
    best_records = get_best_records(song.title)
    for difficulty in song_difficulty:
        song_history.append({"level" : difficulty.level, \
                             "note" : difficulty.note, \
                                "chart_constant" : difficulty.chart_constant,
                                "best_record" : best_records[difficulty.level]})
        
    return song_history
def get_best_records(song_title : str):
    """
    之後要改成從資料庫查詢
    """
    DEFAULT = {"Past" : 0, "Present" : 0, "Future" : 0,\
               "Beyond" : 0, "Eternal" : 0, "Moment" : 0, "Eternity" : 0}

    return DEFAULT

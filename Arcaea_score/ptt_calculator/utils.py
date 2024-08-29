from .models import Song, Record


def get_song_history_data(song : Song, request):
    song_difficulty = song.difficulty_set.all()
    song_history = []
    
    for difficulty in song_difficulty:
        song_history.append({"level" : difficulty.level, \
                             "note" : difficulty.note, \
                                "chart_constant" : difficulty.chart_constant,
                                "best_record" : get_best_records(difficulty, request)})
        
    return song_history
def get_best_records(difficulty, request):
    try:
        return difficulty.record_set.get(user=request.user).record
    except:
        return 0



def edit_add_record(song : Song, request):
    """
    編輯或新增遊玩紀錄
    """
    form_input = request.POST
    difficultys = song.difficulty_set.all()
    for difficulty in difficultys:
        
        player_record = int(form_input[difficulty.level])
        if player_record == 0:
            continue
        try:
            record = difficulty.record_set.get(user=request.user)
            if player_record > record.record:
                record.record = player_record
                record.score = get_score(player_record, difficulty.chart_constant)
                record.save()
        except Record.DoesNotExist:
            new_record = Record(user=request.user, \
                                    difficulty=difficulty, \
                                    record=player_record, \
                                    score=get_score(player_record, difficulty.chart_constant))
            new_record.save()

def get_score(record : int, chart_constant : float):
    if record > 10000000:
        return chart_constant + 2
    elif record > 9800000:
        return chart_constant + 1 + record / 200000
    else:
        return chart_constant + (9500000 - record) / 300000

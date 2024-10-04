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
        if player_record < 0:
            continue
        try:
            record = difficulty.record_set.get(user=request.user)
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
        return chart_constant + 1 + (record - 9800000) / 200000
    else:
        return max(0, chart_constant + (record - 9500000) / 300000)

def get_best_30(request):
    user = request.user
    best_30 = Record.objects.filter(user=user).order_by('-score')
    record_take_num = min(30, len(best_30))

    
    return get_best_30_matrix(best_30[:record_take_num])

def get_best_30_matrix(best_30):
    best_30_matrix = []
    for i in range(5):
        best_30_matrix.append([])
        for j in range(6):
            if 6 * i + j >= len(best_30):
                break
            difficulty = best_30[6 * i + j].difficulty
            song = difficulty.song

            data = {
                "title" : song.title,
                "img" : song.img_url,
                "chart_constant" : difficulty.chart_constant,
                "level" : difficulty.level,
                "score" : round(best_30[6 * i + j].score, 5),
                "record" : best_30[6 * i + j].record
            }
            best_30_matrix[i].append(data)
    return best_30_matrix
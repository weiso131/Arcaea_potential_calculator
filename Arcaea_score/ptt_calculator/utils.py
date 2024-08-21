import requests
from bs4 import BeautifulSoup

ARCAEA_SONGS_URL = "https://arcwiki.mcd.blue"

NOTE_DATA_DICT = {"Past" : "pst-data", 
                  "Present" : "prs-data", 
                  "Future" : "ftr-data", 
                  "Beyond" : "byd-data", 
                  "Eternal" : "byd-data"}

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def get_song_list():
    
    response = requests.get(ARCAEA_SONGS_URL + "/%E6%9B%B2%E7%9B%AE%E5%88%97%E8%A1%A8")
    all_songs = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        song_table = soup.find('table', class_='wikitable sortable')
        if song_table:
            rows = song_table.find_all('tr')
            for i in range(2, len(rows)):
                columns = rows[i].find_all('td')

                song = columns[2].find('a')

                if song is None or columns[7].get_text(strip=True) == '/': #扣掉Last和愚人節的byd
                    continue

                all_songs.append((song.get_text(strip=True), song.get('href')))
                
                
    else:
        print(f"Failed to fetch data from {ARCAEA_SONGS_URL}. Status code: {response.status_code}")

    return all_songs
        
def get_song_data(link):
    response = requests.get(ARCAEA_SONGS_URL + link)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        song_data = get_chart_constants(soup)
        song_data["note"] = get_note(soup, song_data["level"])
        song_data["img"] = get_img_source(soup)
        
        return song_data

    else:
        print(f"Failed to fetch data from {link}. Status code: {response.status_code}")

        return None
def get_chart_constants(soup):
    tables = soup.find_all('table', class_ = "wikitable", style="text-align:center")
    data = {"level" : [], "chart_constants" : []}
    for table in tables:
        if not is_float(table.find('td').get_text(strip=True)) or table.find('th').get_text(strip=True) != "Past":
            continue
        level = table.find_all('tr')[0].find_all('th')
        chart_constants = table.find_all('tr')[1].find_all('td')
        

        for i in range(len(level)):
            data["level"].append(level[i].get_text(strip=True))
            data["chart_constants"].append(float(chart_constants[i].get_text(strip=True)))
        break
    return data

def get_note(soup, levels : list):
    note_data = []
    for level in levels:
        note_data.append(int(soup.find_all('div', class_ = NOTE_DATA_DICT[level])[1].get_text(strip=True)))
    return note_data

def get_img_source(soup):
    img_src = soup.find('div', class_ = "floatnone").find('img').get('src')
    return ARCAEA_SONGS_URL + img_src

get_song_data("/ALTER_EGO")
import sys, re
import requests
import urllib.request, urllib.error
from bs4 import BeautifulSoup

def clean_lyrics(lyrics):
    lyric_list = list(filter(lambda x: x != '\n', lyrics))
    lyric_list = list(map(lambda x: x.strip('\r').strip('\n'), lyric_list))[1:]

    return lyric_list

def clean_names(artist_name, song_name):
    artist_name = re.sub(r"[^a-zA-Z0-9_]", '', artist_name.lower().replace(' ', ''))
    song_name = re.sub(r"[^a-zA-Z0-9_]", '', song_name.lower().replace(' ', ''))

    return artist_name, song_name

def extract_lyrics(artist, song):
    artist_name, song_name = clean_names(artist, song)
    url = create_url(artist_name, song_name)
    page = get_page(url)
    soup = BeautifulSoup(page, 'html.parser')
    mydivs = soup.find("div", {"class": "ringtone"})
    lyrics = mydivs.find_next_sibling("div")
    lyric_list = []
    for line in lyrics:
        try:
            if "<br/>" not in line.string:
                lyric_list.append(line.string)
        except TypeError:
            pass

    lyric_list = clean_lyrics(lyric_list)
    return lyric_list

def create_url(artist_name, song_name):
    return "https://www.azlyrics.com/lyrics/{}/{}.html".format(artist_name, song_name)

def get_page(url):
    try:
        page = urllib.request.urlopen(url)
        return page.read()
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print("Music not found")
            sys.exit(1)

if __name__ == "__main__":
    # a_name, s_name = clean_names("Metallica", "...And Justice For All")
    # # print(a_name, s_name)
    # url = create_url(a_name, s_name)
    # pg = get_page(url)
    # lyr = extract_lyrics(pg)
    # clean_lyr = clean_lyrics(lyr)
    # print(clean_lyr)
    pass
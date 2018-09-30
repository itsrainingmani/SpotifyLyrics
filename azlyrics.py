import sys, re
import requests
import urllib.request, urllib.error
from bs4 import BeautifulSoup
from colorama import init, Fore


def clean_lyrics(lyrics):
    lyric_list = list(filter(lambda x: x != "\n", lyrics))
    lyric_list = list(map(lambda x: x.strip("\r").strip("\n"), lyric_list))[1:]

    return lyric_list


def pretty_print_lyrics(lyric_list):
    for i in range(0, len(lyric_list)):
        print(lyric_list[i])
        if (i + 1) % 4 == 0 and i > 0:
            print("\n")
            # pass
    print("\n")


def color_print_title(data):
    print(Fore.RED + "\r{} by {}\n\n".ljust(10, " ").format(data[0], data[1]), end="")


def color_print_progress(progress):
    print(Fore.GREEN + "\rProgress - {}%".ljust(20, " ").format(progress), end="")


def color_print_error():
    print(Fore.RED + "\rNo Track is playing", end="")


def clean_names(artist_name, song_name):
    artist_name = re.sub(r"^The", "", artist_name)
    artist_name = re.sub(r"[^a-zA-Z0-9_]", "", artist_name.lower().replace(" ", ""))
    song_name = re.sub(r"[^a-zA-Z0-9_]", "", song_name.lower().replace(" ", ""))

    return artist_name, song_name


def create_url(artist_name, song_name):
    return "https://www.azlyrics.com/lyrics/{}/{}.html".format(artist_name, song_name)


def get_page(url):
    try:
        page = urllib.request.urlopen(url)
        return page.read()
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return "Lyrics not found"


def extract_lyrics(artist, song):
    artist_name, song_name = clean_names(artist, song)
    # print(artist_name, song_name)
    url = create_url(artist_name, song_name)
    page = get_page(url)
    if page == "Lyrics not found":
        return [page]
    soup = BeautifulSoup(page, "html.parser")
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


if __name__ == "__main__":
    # a_name, s_name = clean_names("Metallica", "...And Justice For All")
    # # print(a_name, s_name)
    # url = create_url(a_name, s_name)
    # pg = get_page(url)
    # lyr = extract_lyrics(pg)
    # clean_lyr = clean_lyrics(lyr)
    # print(clean_lyr)
    pass

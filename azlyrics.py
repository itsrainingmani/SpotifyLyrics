import re
from bs4 import BeautifulSoup

def extract(soup):
    mydivs = soup.find("div", {"class": "ringtone"})
    lyrics = mydivs.find_next_sibling("div")

    lyric_list = []

    for line in lyrics:
        try:
            if "<br/>" not in line.string:
                lyric_list.append(line.string)
        except TypeError:
            pass
        
    lyric_list = list(filter(lambda x: x != '\n', lyric_list))
    lyric_list = list(map(lambda x: x.strip('\n'), lyric_list))[1:]

    return lyric_list

if __name__ == "__main__":
    html_doc = open('./lyrics_test/Metallica-Blackened.html')
    soup = BeautifulSoup(html_doc, 'html.parser')

    for line in extract(soup):
        print(line + '\n')

import re
from bs4 import BeautifulSoup

html_doc = open('Metallica-One.html')
soup = BeautifulSoup(html_doc, 'html.parser')

mydivs = soup.find("div", {"class": "ringtone"})
lyrics = mydivs.find_next_sibling("div")
# regex = re.compile(r"")
count = 0


for line in lyrics:
    count += 1
    try:
        if "<br/>" not in line.string:
            print(count, line.string)
    except TypeError:
        pass
    
print(type(lyrics))

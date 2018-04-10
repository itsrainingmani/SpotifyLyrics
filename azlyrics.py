from bs4 import BeautifulSoup

html_doc = open('Metallica-One.html')
soup = BeautifulSoup(html_doc, 'html.parser')

mydivs = soup.find("div", {"class": "ringtone"})
print(mydivs.find_next_siblings("div"))
# for div in soup.find_all('div'):
#     if "class" in div.attrs.keys():
#         # print(div['class'])
#         if "ringtone" in div['class']:
#             print(div)

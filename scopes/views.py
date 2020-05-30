from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


#  ASTROLOGY
ast_link = requests.get("https://www.astrology.com/horoscope/daily/scorpio.html")
soup = BeautifulSoup(ast_link.content, 'html5lib')

headings = soup.findAll("p")
headings = headings[0:1]

ast_scopes = []

for th in headings:
    ast_scopes.append(th.text)


# ELLE
elle_link = requests.get("https://www.elle.com/horoscopes/daily/a104/scorpio-daily-horoscope/")
soup = BeautifulSoup(elle_link.content, 'html5lib')

headings = soup.findAll("p", {"class": "body-text"})
headings = headings[0:1]

elle_scopes = []

for th in headings:
    elle_scopes.append(th.text)

# ASTROYOGI
yogi_link = requests.get("https://www.astroyogi.com/horoscopes/daily/scorpio-free-horoscope.aspx")
soup = BeautifulSoup(yogi_link.content, 'html5lib')

headings = soup.findAll("p", {"class": "line27"})
headings = headings[1:2]

yogi_scopes = []

for th in headings:
    yogi_scopes.append(th.text)

# ASTROSTYLE
style_link = requests.get("https://astrostyle.com/horoscopes/daily/scorpio/")
soup = BeautifulSoup(style_link.content, 'html5lib')

headings = soup.find("div", {"class": "horoscope-content"})
# headings = headings[1:2]

astro_scopes = []

for th in headings.findAll('p'):
    astro_scopes.append(th.text)

# DAILY-HOROSCOPE
daily_link = requests.get("https://www.dailyhoroscope.com/horoscopes/daily/scorpio?full=true")
soup = BeautifulSoup(daily_link.content, 'html5lib')

headings = soup.findAll("p", {"class": "body"})
headings = headings[0:1]

daily_scopes = []

for th in headings:
    daily_scopes.append(th.text)

def index(req):
    return render(req, 'scopes/index.html', {'ast_scopes': ast_scopes, 'elle_scopes': elle_scopes, 'yogi_scopes': yogi_scopes, 'astro_scopes': astro_scopes, 'daily_scopes': daily_scopes})
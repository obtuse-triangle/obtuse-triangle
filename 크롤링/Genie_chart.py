import requests
from bs4 import BeautifulSoup
import re


def clean_text(text):
    cleaned_text = " ".join(re.split("\s+", text, flags=re.UNICODE))
    return cleaned_text

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
}
url = 'https://www.genie.co.kr/chart/top200'
resp = requests.get(url, headers = headers)
soup = BeautifulSoup(resp.text, 'html.parser')
songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
i = 0
a = [0]

for song in songs:
    i+=1
    a.append(clean_text(f'[{i}위]' + song.find('td',{'class':'info'}).find('a',{'class':'title ellipsis'}).text))
    
i = 0

while i != 50:
    i+=1
    print(a[i])

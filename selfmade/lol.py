import requests
from bs4 import BeautifulSoup
import re
import time

source_code = requests.get('https://erotik-whv.de/')
soup = BeautifulSoup(source_code.content, 'lxml')
data = []
links = []


def remove_duplicates(l): # remove duplicates and unURL string
    for item in l:
        match = re.search("(?P<url>https?://[^\s]+)", item)
        if match is not None:
            links.append((match.group("url")))


for link in soup.find_all('a', href=True):
    data.append(str(link.get('href')))
print(data)
flag = True
remove_duplicates(data)
while flag:
    try:
        for link in links:
            for j in soup.find_all('a', href=True):
                temp = []
                source_code = requests.get(link)
                soup = BeautifulSoup(source_code.content, 'lxml')
                temp.append(str(j.get('href')))
                remove_duplicates(temp)

                if len(links) > 169: # set limitation to number of URLs
                    break
            if len(links) > 160:
                break
        if len(links) > 160:
            break
    except Exception as e:
        print(e)
        if len(links) > 160:
            break

for url in links:
    print(url)
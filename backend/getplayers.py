#!/usr/bin/env python3

from urllib.request import urlopen
from bs4 import BeautifulSoup

data = urlopen('http://www.cfbstats.com/2014/team/140/roster.html')
soup = BeautifulSoup(data.read()) # creates a BS4 HTML parsing object

for row in soup('tr')[1:]:
    data = [str(i.getText()) for i in row('td')]
    link = row('td')[1]('a') # the linked player
    if len(link) > 0:
        link = str(link[0]['href'])
        data = [str(link)] + data
    print(data)
    print('\n')
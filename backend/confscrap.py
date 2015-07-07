#!/usr/bin/env python3

from urllib.request import urlopen
from bs4 import BeautifulSoup

data = urlopen('https://en.wikipedia.org/wiki/List_of_NCAA_conferences')
soup = BeautifulSoup(data.read(), "html.parser")

soup_data = soup.findAll("td")

for conf_info in soup_data :
	conf_help = conf_info.text
	if conf_help == 'Big Sky Conference' :
		break
	print(conf_help)
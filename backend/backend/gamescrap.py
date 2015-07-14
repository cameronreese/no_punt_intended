#!/usr/bin/env python3

from urllib.request import urlopen
from bs4 import BeautifulSoup

data = urlopen('http://www.fbschedules.com/ncaa/2015-college-football-schedules.php')
soup = BeautifulSoup(data.read(), "html.parser")

soup_data = soup.findAll("ul")

for game_info in soup_data :
	game_help = game_info.findAll("li")
	for game_help2 in game_help :
		print(game_help2)
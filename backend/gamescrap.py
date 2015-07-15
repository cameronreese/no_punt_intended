#!/usr/bin/env python3

from urllib.request import urlopen
from bs4 import BeautifulSoup

data = urlopen('http://www.jhowell.net/cf/scores/Sked2015.htm')
soup = BeautifulSoup(data.read(), "html.parser")

soup_data = soup.findAll("tr")
game_dict = {}
g_away = []
g_home = []
temp_team = ''
g_date = []
decider = ''
j = 1
for game_info in soup_data :
	game_help = game_info.findAll("td")
	i = 1
	# print(j)
	for game_help2 in game_help :
		# print(i)
		game_help3 = game_help2.text
		# print(game_help3)
		if i == 1 :
			temp_help = game_help3.split(' (')
			if len(temp_help) > 1 :
				temp_team = temp_help[0]
				# print(temp_team)
			else :
				if(temp_help[0] != '\xa0') :
					g_date += temp_help
				# print(g_date)
		if i == 3 :
			decider = game_help3
		if i == 4:
			if decider == '@' :
				g_away.append(temp_team)
				g_home.append(game_help3) 
			else :
				g_home.append(temp_team)
				g_away.append(game_help3)
		# print(game_help3)
		# print(i)
		i+=1
	# print(j)
	j+=1
	# print(game_help)
# print(g_away)
# print(len(g_away))
# print(g_home)
# print(len(g_home))
# print(g_date)
# print(len(g_date))
gid = 1
k = 0

while k < len(g_away) :
	dict_help = {}
	dict_help['date'] = g_date[k]
	temp = g_away[k]
	if temp[0] == '*' :
		temp2 = temp[1:]
		if temp2 == 'Texas-El Paso' :
			temp2 = 'UTEP'
		if temp2 == 'Nevada-Las Vegas' :
			temp2 = 'UNLV'
	else :
		temp2 = temp
		if temp2 == 'Texas-El Paso' :
			temp2 = 'UTEP'
		if temp2 == 'Nevada-Las Vegas' :
			temp2 = 'UNLV'
	dict_help['away'] = temp2
	temp = g_home[k]
	if temp[0] == '*' :
		temp2 = temp[1:]
		if temp2 == 'Texas-El Paso' :
			temp2 = 'UTEP'
		if temp2 == 'Nevada-Las Vegas' :
			temp2 = 'UNLV'
	else :
		temp2 = temp
		if temp2 == 'Texas-El Paso' :
			temp2 = 'UTEP'
		if temp2 == 'Nevada-Las Vegas' :
			temp2 = 'UNLV'
	dict_help['home'] = temp2
	dict_help['time'] = 'TBA'
	game_dict[gid] = dict_help
	gid+=1
	k+=1

import json
with open('game.json','w+') as out :
	json.dump(game_dict,out)
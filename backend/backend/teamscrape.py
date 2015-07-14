#!/usr/bin/env python3

from urllib.request import urlopen
from bs4 import BeautifulSoup

data = urlopen('https://en.wikipedia.org/wiki/List_of_NCAA_Division_I_FBS_football_programs')
soup = BeautifulSoup(data.read(), "html.parser")

soup_data = soup.findAll("td")
team_name = []
team_conf = []
team_loc = []
team_coach = []
team_nick = []
team_dict = {}
namecount = 0
nickcount = 0
confcount = 0
loccount = 0
coachcount = 0
i = 1
for team_info in soup_data :
	team_help = team_info.text
	team_help2 = team_help.split('\n')
	if team_help == 'UAB' :
		break
	if i == 1 :
		team_name.append(team_help2[0])
		# print(team_help2[0])
		namecount += 1
			
	if i == 2 :
		cool = team_info.find("a")
		if len(team_help2) > 1 :
			team_nick.append(team_help2[0] + " " + team_help2[1])
			nickcount += 1
		else :
			team_nick.append(team_help)
			nickcount += 1
		if team_help == 'Miners':
			print('got here')
			team_coach.append('Sean Kugler')
		else :
			team_url = ('https://en.wikipedia.org' + cool['href'])
			data2 = urlopen(team_url)
			soup2 = BeautifulSoup(data2.read(), "html.parser")
			soup_data2 = soup2.findAll("tr")
			for get_coach in soup_data2 :
				team_help3 = get_coach.text
				team_help4 = team_help3.split('\n')
				if team_help4[1] == 'Head coach' :
					team_coach.append(team_help4[2])
					coachcount += 1

				# print(namecount)
				# print(coachcount)
			# if team_help4[1] == 'Head Coach' :
			# 	team_coach.append(team_help4[2])
			# 	coachcount += 1
			# else :
			# 	team_coach.append('None')
	if i == 3 :
		team_loc.append(team_help2[0])
		loccount += 1
	if i == 5 :
		team_conf.append(team_help2[0])
		confcount += 1
	if i % 8 == 0 :
		i = 0 
	i += 1
# print(namecount)
# print(confcount)
# print(loccount)
# print(coachcount)
# print(nickcount)
#print(conf_url)
x = 0
for y in team_name :
	dict_help = {}
	dict_help['nick'] = team_nick[x]
	dict_help['coach'] = team_coach[x]
	dict_help['location'] = team_loc[x]
	dict_help['conference'] = team_conf[x]
	
# 	if x == 5 :
# 		dict_help['coach'] = 'None'
# 	if x > 5 :
# 		dict_help['coach'] = team_coach[x-1]
# 	if x < 5 :
# 		dict_help['coach'] = team_coach[x]
	team_dict[y] = dict_help
	x+=1
# print(team_dict)
#print(conf_names)
#print(conf_nick)
#print(conf_founded)
#print(conf_comm)
#print(conf_num)
import json
with open('team.json','w+') as out :
	json.dump(team_dict,out)
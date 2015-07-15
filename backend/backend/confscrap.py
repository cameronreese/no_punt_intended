#!/usr/bin/env python3

from urllib.request import urlopen
from bs4 import BeautifulSoup

data = urlopen('https://en.wikipedia.org/wiki/List_of_NCAA_conferences')
soup = BeautifulSoup(data.read(), "html.parser")

soup_data = soup.findAll("td")
conf_names = []
conf_founded = []
conf_num = []
conf_comm = []
conf_nick = []
conf_dict = {}

# The data is scraped from first page and enters the conference's page to extract commissioner
# The final dictionary helps produce the json out file
i = 1
for conf_info in soup_data :
	cool = conf_info.find("a")
	conf_help = conf_info.text
	conf_help2 = conf_help.split('\n')
	#break once the page gets to FCS teams
	if conf_help == 'Big Sky Conference' :
		break
	if i == 1 :
		if len(conf_help2) == 2 :
			conf_names.append(conf_help2[0] + " " + conf_help2[1])
		else :
			conf_names.append(conf_help)
		conf_url = ('https://en.wikipedia.org'+cool['href'])
		data2 = urlopen(conf_url)
		soup2 = BeautifulSoup(data2.read(), "html.parser")
		soup_data2 = soup2.findAll("tr")
		for get_com in soup_data2 :
			conf_help3 = get_com.text
			conf_help4 = conf_help3.split('\n')
			if conf_help4[1] == 'Commissioner' :
				conf_comm.append(conf_help4[2])	
	if i == 2 :
		conf_nick.append(conf_help2[0])
	if i == 3 :
		conf_founded.append(conf_help2[0])
	if i == 4 :
		conf_num.append(conf_help2[0])
	if i % 7 == 0 :
		i = 0 
	i += 1
#print(conf_url)
x = 0
for y in conf_names :
	dict_help = {}
	dict_help['name'] = conf_nick[x]
	dict_help['founded'] = conf_founded[x]
	dict_help['num_teams'] = conf_num[x]
	if x == 5 :
		dict_help['comm'] = 'None'
	if x > 5 :
		dict_help['comm'] = conf_comm[x-1]
	if x < 5 :
		dict_help['comm'] = conf_comm[x]
	conf_dict[y] = dict_help
	x+=1
# print(conf_dict)
#print(conf_names)
#print(conf_nick)
#print(conf_founded)
#print(conf_comm)
#print(conf_num)
import json
with open('conf.json','w+') as out :
	json.dump(conf_dict,out)
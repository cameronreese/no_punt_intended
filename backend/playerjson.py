#!/usr/bin/env python3
import json
import sys

player_dict = {}

players = None
player_pic = None
players = open("../backend/newPlayers.txt", 'r')
player_pic = open("../backend/key", 'r')
pic_dict={}
help_pic =''
for getpic in player_pic :
	help_pic = str(getpic)
to = 1
pname=''
ppic=''
for z in help_pic.split(', '):
	for g in z.split(': ') :
		if to == 1 :
			pname = g[2:len(g)-1]
			# print(pname)
		if to%2 and to >1 :
			pname = g[1:len(g)-1]
			# print(pname)
		if to == 9380 :
			ppic = g[1:len(g)-2]
		if to%2 == 0 :
			ppic = g[1:len(g)-1]
		to+=1
	pic_dict[pname] = ppic
# print(pic_dict)

def isKey(name) :
	for p in pic_dict :
		if p == name :
			return True
	return False		

p_id = 1
for line in players :
	if len(line) > 1 :
		line_help = str(line)
		i = 1
		first = ''
		last = ''
		name = ''
		no = ''
		team = ''
		year = ''
		pos = ''
		ht = ''
		wt = ''
		city = ''
		st = ''
		hometown = ''
		hs = ''
		pic = ''

		for line2 in line_help.split(", ") :
			if i == 1 :
				team = line2
			if i == 2 :
				if line2[len(line2)-1] == 'A' :
					no = line2[:len(line2)-1]
				else :
					no = line2
			if i == 3 :
				last = line2
			if i == 4 :
				if line2 == 'Jr' :
					i = 3
					# print("****\n")
					# print(last)
					temp = line2[:len(line2)-1]
					tempL = last
					last = (tempL + ' ' + temp)
				else :
					first = line2
					name = (first+' '+last)
					if(isKey(name.lower())) :
						pic = pic_dict[name.lower()]
					else :
						pic = ''
				# print(pic)
			if i == 5 :
				pos = line2
			if i == 6 :
				year = line2
			if i == 7 :
				ht = line2
			if i == 8 :
				wt = line2
			if i == 9 :
				city = line2
			if i == 10 :
				st = line2
				hometown = (city + ', ' + st)
			if i == 11 :
				hs = line2[:len(line2)-1]
			#print(line2)
			i+=1
		# print(team)
		# print(no)
		# print(name)
		# print(pos)
		# print(year)
		# print(ht)
		# print(wt)
		# print(hometown)
		# print(hs)
		dict_help = {}
		dict_help['name'] = name
		dict_help['no'] = no
		dict_help['pos'] = pos
		dict_help['team'] = team
		dict_help['ht'] = ht
		dict_help['wt'] = wt
		dict_help['hometown'] = hometown
		dict_help['year'] = year
		dict_help['hs'] = hs
		dict_help['pic'] = pic
		player_dict[p_id] = dict_help
		p_id+=1
# print(player_dict)

with open('player.json','w+') as out :
	json.dump(player_dict,out)

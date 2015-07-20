#!/usr/bin/env python3

import json
import sys

with open("../backend/game.json") as fjg:
		games = json.load(fjg)
i = 1

iddict = {}
for id1 in games :
	with open("../backend/game.json") as fjg:
		games_help = json.load(fjg)
	id1_info = games[id1]
	for id2 in games_help :
		id2_info = games_help[id2]
		if id1 != id2 and id1_info['date'] == id2_info['date'] and id1_info['home'] == id2_info['home'] and id1_info['away'] == id2_info['away'] and id1 not in iddict:
			iddict[id2] = 'DELETETHIS'
	i+=1

for id3 in iddict :
	games.pop(id3)

with open('newgames.json', 'w+') as out :
	json.dump(games, out)
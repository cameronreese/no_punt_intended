#!/usr/bin/env python3

# -----------
# imports
# -----------
from models import players, teams, conf, games, schedule
from flask import Flask
from models import punt, db
import json
import sys

players_json
teams_json
conf_json
games_json

with open("../backend/player.json") as fj:
	players_json = json.load(fj)

with open("../backend/team.json") as fj:
	teams_json = json.load(fj)

with open("../backend/conf.json") as fj:
	conf_json = json.load(fj)

# with open("../backend/game.json") as fj:
# 	games_json = json.load(fj)

def fill() :

	db.session.remove()
	db.drop_all()
	db.create_all()

	for c_name in conf_json :
		c_info = conf_json[cname]
		c_data = conf(name = c_info['name'],
			founded = c_info['founded'],
			num_teams = c_info['num_teams'],
			comm = c_info['comm'])
		db.session.add(c_data)
		db.session.commit()

	for t_name in teams_json :
		t_info = teams_json[t_name]
		t_data = teams(name = t_name,
			location = t_info['location'],
			head_coach = t_info['coach'],
			conf = t_info['conference'])
		db.session.add(t_data)
		db.session.commit()

	for p_id in players_json :
		p_info = players_json[p_id]
		p_data = players(id = p_id,
			name = p_info['name'],
			no = p_info['no'],
			pos = p_info['pos'],
			team = p_info['team'],
			ht = p_info['ht'],
			wt = p_info['wt'],
			hometown = p_info['hometown'],
			year = p_info['year'],
			hs = p_info['hs'],
			photo = p_info['photo'])
		db.session.add(p_data)
		db.session.commit()

	# for g_id in games_json :
	# 	g_info = games_json[g_id]
	# 	g_data = games(id = g_id,
	# 		date = g_info['date'],
	# 		home_team = g_info['home_team'],
	# 		away_team = g_info['away_team'],
	# 		location = g_info['location'],
	# 		time = g_info['time'])
	# 	db.session.add(g_data)
	# 	db.session.commit()

	# sched = games.query.all()
	# for s_data in sched :
	# 	home = 
	# 	away = s_data.away_team
	# 	db.session.execute(schedule.insert().values([s_data.home_team,s_data.id]))
	# 	db.session.commit()
	# 	db.session.execute(schedule.insert().values([s_data.away_team,s_data.id]))
	# 	db.session.commit()

if __name__ == '__main__':
	fill()

#!/usr/bin/env python3

# -----------
# imports
# -----------
from models import players, teams, conf, games, schedule
from flask import Flask
from models import punt, db
import json
import sys


def fill():
	print('entered fill()')
	db.session.remove()
	print('db.session.remove()...')
	db.drop_all()
	print('db.drop_all()...')
	db.create_all()
	print('db.create_all()...')

	for c_name in conf_json :
		print('here in the first for loop')
		c_info = conf_json[c_name]
		c_data = conf(name = c_info['name'],
			founded = c_info['founded'],
			num_teams = c_info['num_teams'],
			comm = c_info['comm'],
			champ = c_info['champ'])
		db.session.add(c_data)
		db.session.commit()
		print('conf made')

	for t_name in teams_json :
		print('entered teams building...')
		t_info = teams_json[t_name]
		t_data = teams(name = t_name,
			location = t_info['location'],
			head_coach = t_info['coach'],
			confname = t_info['conference'])
		db.session.add(t_data)
		db.session.commit()
		print('team made')

	for p_id in players_json :
		p_info = players_json[p_id]
		if (p_info['team'] != 'UAB'):
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
				photo = p_info['pic'])
			db.session.add(p_data)
			db.session.commit()
	print('players made')

	for g_id in games_json :
		g_info = games_json[g_id]
		away_t = "NOT FBS"
		home_t = "NOT FBS"
		if g_info['away'] in teams_json:
			away_t = g_info['away']
		if g_info['home'] in teams_json:
			home_t = g_info['home']
		g_data = games(id = g_id,
			date = g_info['date'],
			home_team = home_t,
			away_team = away_t,
			location = 'TBD',
			time = g_info['time'])
		db.session.add(g_data)
		db.session.commit()
	print('games made')

	sched = games.query.all()
	for s_data in sched :
		home = s_data.home_team
		away = s_data.away_team
		db.session.execute(schedule.insert().values([s_data.home_team,s_data.id]))
		db.session.commit()
		db.session.execute(schedule.insert().values([s_data.away_team,s_data.id]))
		db.session.commit()
	print('schedule made')


if __name__ == '__main__':
	print('started program')
	with open("./backend/player.json") as fjp:
		players_json = json.load(fjp)

	with open("./backend/team.json") as fjt:
		teams_json = json.load(fjt)

	with open("./backend/conf.json") as fjc:
		conf_json = json.load(fjc)

	with open("./backend/newgames.json") as fjg:
		games_json = json.load(fjg)
	print('about to enter fill function')
	fill()
	print('just finished fill()')


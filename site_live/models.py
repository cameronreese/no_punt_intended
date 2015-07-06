#!/usr/bin/env python3

# -----------
# imports
# -----------
import random
from numpy import mean, sqrt, square, subtract
import json

from flask import Flask
from flask import jsonify
from flask import abort

punt = Flask(__name__)

""" Temporary data structures until we have a data base set up """

# players model
players = [
    {
        'name': 'Nick Jordan',
        'no': '#28',
        'pos': 'PK',
        'team': 'Texas Longhorns',
        'ht': '6-1',
        'wt': '193',
        'hometown': 'Coppell, TX',
    },
    {
        'name': 'Shiro Davis',
        'no': '#1',
        'pos': 'DE',
        'team': 'Texas Longhorns',
        'ht': '6-3',
        'wt': '265',
        'hometown': 'Shreveport, LA',
    },
    {
        'name': 'Jeff Bryson',
        'no': '#59',
        'pos': 'LB',
        'team': 'Baylor Bears',
        'ht': '5-10',
        'wt': '200',
        'hometown': 'San Antonio, TX',
    },
]

teams = [
    {
        'name': 'Texas Longhorns',
        'location': 'Austin, TX',
        'roster': (), # tuple of player links
        'schedule': [[]], # a dict of {date : opponent} or some custom list of data
        'head_coach': 'Strong',
        'conf': 'Big 12'
    },
    {
        'name': 'Baylor Bears',
        'location': 'Waco, TX',
        'roster': (), # tuple of player links
        'schedule': [[]], # a dict of {date : opponent} or some custom list of data
        'head_coach': 'Unknown',
        'conf': 'Big 12'
    },
    {
        'name': 'TCU Horned Frogs',
        'location': 'Fort Worth, TX',
        'roster': (), # tuple of player links
        'schedule': [[]], # a dict of {date : opponent} or some custom list of data
        'head_coach': 'Unknown',
        'conf': 'Big 12'
    }
]

conf = [
    {
        'name': 'Big 12',
        'founded': 'some year',
        'current_conf_champion': 'team',
        'teams': [], # list of teams
        'number_of_teams': 'a_num'
    }
]

@punt.route('/punt/players/<string:player_name>', methods=['GET'])
def get_players(player_name):
    if player_name == 'players':
        return jsonify({'players': players})

    player = [player for player in players if player['name'] == player_name]
    if len(player) == 0:
        abort(404)
    return jsonify({'players': player[0]})

@punt.route('/punt/teams/<string:team_name>', methods=['GET'])
def get_teams(team_name):
    if team_name == 'teams':
        return jsonify({'teams': teams})

    team = [team for team in teams if team['name'] == team_name]
    if len(team) == 0:
        abort(404)
    return jsonify({'teams': team[0]})

@punt.route('/punt/conf/<string:conf_name>', methods=['GET'])
def get_conf(conf_name):
    if conf_name == 'conf':
        return jsonify({'conf': conf})

    c = [c for c in conf if c['name'] == conf_name]
    if len(c) == 0:
        abort(404)
    return jsonify({'conf': c[0]})

if __name__ == '__main__':
    punt.run(debug=True)

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
from flask import render_template
from collections import namedtuple
from urllib.request import urlopen
from flask.ext.sqlalchemy import SQLAlchemy


punt = Flask(__name__)

'''
punt.config['SQLALCHEMY_DATABASE_URI] = 'mysql+pymysql://username:password@host:port/database'

db = SQLAlchemy(punt)

# players model
class players(db.Model) :
    id = db.Column(db.Integer,primary_key = True,unique = True,index = True)
    name = db.Column(db.String(256))
    no = db.Column(db.String(256))
    pos = db.Column(db.String(256))
    team = db.Column(db.String(256),db.ForeignKey(teams.name))
    ht = db.Column(db.String(256))
    wt = db.Column(db.String(256))
    hometown = db.Column(db.String(256))
    year = db.Column(db.String(256))
    hs = db.Column(db.String(256))
    photo = db.Column(db.String(256))

schedule = db.Table('schedule',db.Column('teams_name',db.String(256),db.ForeignKey('teams.name')),db.Column('game_id',db.Integer,db.ForeignKey('games.id')))

# teams model
class teams(db.Model) :
    name = db.Column(db.String(256),primary_key = True)
    location = db.Column(db.String(256))
    roster = db.relationship('players',backref = 'teams', lazy = 'dynamic')
    schedule = db.relationship('games',secondary=schedule,backref=db.backref('teams',lazy='dynamic'))
    head_coach = db.Column(db.String(256))
    conf = db.Column(db.String(256),db.ForeignKey(conf.name))

# conference model
class conf(db.Model) :
    name = db.Column(db.String(256),primary_key = True)
    founded = db.Column(db.String(256))
    champ = db.Column(db.String(256))
    teams = db.relationship('teams',backref = 'conf', lazy = 'dynamic')
    num_teams = db.Column(db.String(256))
    comm = db.Column(db.String(256))

# games model
class games(db.Model) :
    id = db.Column(db.Integer,primary_key = True,unique = True,index = True)
    date = db.Column(db.String(256))
    opponent = db.Column(db.String(256),db.ForeignKey(teams.name))
    location = db.Column(db.String(256),db.ForeignKey(teams.location))
    time = db.Column(db.String(256))
'''

""" Temporary data structures until we have a data base set up """

# players model
players = [
    {
        'name': 'Nick Jordan',
        'no': '28',
        'pos': 'PK',
        'team': 'Texas',
        'ht': '6-1',
        'wt': '193',
        'hometown': 'Coppell, TX',
        'year': 'S',
        'hs': 'Coppell',
        'photo': 'http://texassports.com/common/controls/image_handler.aspx?thumb_prefix=player&image_path=/images/2013/6/25/7930078.jpeg'
    },
    {
        'name': 'Shiro Davis',
        'no': '1',
        'pos': 'DE',
        'team': 'Texas',
        'ht': '6-3',
        'wt': '265',
        'hometown': 'Shreveport, LA',
        'year': 'S',
        'hs': 'Coppell',
        'photo': 'http://texassports.com/common/controls/image_handler.aspx?thumb_prefix=player&image_path=/images/2013/6/25/7930067.jpeg'
    },
    {
        'name': 'Jeff Bryson',
        'no': '59',
        'pos': 'LB',
        'team': 'Baylor',
        'ht': '5-10',
        'wt': '200',
        'hometown': 'San Antonio, TX',
        'year': 'S',
        'hs': 'Coppell',
        'photo': 'http://www.baylorbears.com/sports/m-footbl/mtt/jeff_bryson_953393.html'
    },
]

# teams model
teams = [
    {
        'name': 'Texas',
        'location': 'Austin, TX',
        'roster': ['Nick Jordan', 'Shiro Davis'], # list of players
        'schedule': ['1st game', '2nd game', 'last game'], # data of schedule
        'head_coach': 'Charlie Strong',
        'conf': 'Big 12'
    },
    {
        'name': 'Baylor'
        # 'location': 'Waco, TX',
        # 'roster': (), # tuple of player links
        # 'schedule': [[]], # a dict of {date : opponent} or some custom list of data
        # 'head_coach': 'Unknown',
        # 'conf': 'Big 12'
    },
    {
        'name': 'TCU'
        # 'location': 'Fort Worth, TX',
        # 'roster': (), # tuple of player links
        # 'schedule': [[]], # a dict of {date : opponent} or some custom list of data
        # 'head_coach': 'Unknown',
        # 'conf': 'Big 12'
    }
]

# conferences model
conf = [
    {
        'name': 'Big 12',
        'founded': '1996',
        'champ': 'Baylor',
        'teams': ['Baylor', 'Iowa State', 'Kansas', 'Kansas State', 'Oklahoma', 'Oklahoma State', 'TCU', 'Texas', 'Texas Tech', 'West Virginia' ], # list of teams
        'num_teams': '10',
        'comm': 'Bob Bowlsby'
    },
    {
        'name': 'ACC',
        'founded': '1996',
        'champ': 'Baylor',
        'teams': ['Baylor', 'Iowa State', 'Kansas', 'Kansas State', 'Oklahoma', 'Oklahoma State', 'TCU', 'Texas', 'Texas Tech', 'West Virginia' ], # list of teams
        'num_teams': '10',
        'comm': 'Bob Bowlsby'
    },
    {
        'name': 'Big Ten',
        'founded': '1996',
        'champ': 'Baylor',
        'teams': ['Baylor', 'Iowa State', 'Kansas', 'Kansas State', 'Oklahoma', 'Oklahoma State', 'TCU', 'Texas', 'Texas Tech', 'West Virginia' ], # list of teams
        'num_teams': '10',
        'comm': 'Bob Bowlsby'
    },
    {
        'name': 'Nick\'s Own Conf',
        'founded': '2015',
        'champ': 'Nick',
        'teams': ['Baylor', 'Iowa State', 'Kansas', 'Kansas State', 'Oklahoma', 'Oklahoma State', 'TCU', 'Texas', 'Texas Tech', 'West Virginia' ], # list of teams
        'num_teams': '1001',
        'comm': 'Nick the Slick'
    }
]


# *********************************************************************************************************************
# API calls to retrieve model specific data
# *********************************************************************************************************************

@punt.route('/punt/players/<string:player_name>', methods=['GET'])
def get_players(player_name):
    """ GET method
        takes in a player's name as an argument from an http URL 
        and returns json object of the players attributes 
        to retrieve info for all players use 'players' as input
    """
    if player_name == 'players':
        return jsonify({'players': players})
    player = [player for player in players if player['name'] == player_name]
    if len(player) == 0:
        abort(404)
    return jsonify(player[0])

@punt.route('/punt/teams/<string:team_name>', methods=['GET'])
def get_teams(team_name):
    """ GET method
        takes in a team's name as an argument from an http URL 
        and returns json object of the team's attributes 
        to retrieve info for all teams use 'teams' as input
    """
    if team_name == 'teams':
        return jsonify({'teams': teams})

    team = [team for team in teams if team['name'] == team_name]
    if len(team) == 0:
        abort(404)
    return jsonify(team[0])

@punt.route('/punt/conf/<string:conf_name>', methods=['GET'])
def get_conf(conf_name):
    """ GET method
        takes in a conference's nickname as an argument from an http URL 
        and returns json object of the conference's attributes
        to retrieve info for all conferences use 'conf' as input
    """
    if conf_name == 'conf':
        return jsonify({'conf': conf})

    c = [c for c in conf if c['name'] == conf_name]
    if len(c) == 0:
        abort(404)
    return jsonify(c[0])


# *********************************************************************************************************************
# End of API calls to retrieve model specific data  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# *********************************************************************************************************************




# *********************************************************************************************************************
# Template API calls for populating website MAIN static pages
# *********************************************************************************************************************

@punt.route('/')
@punt.route('/index')
def index():
    """
    :return:splash page
    """
    return render_template('index.html', title='CFDB')

@punt.route('/')
@punt.route('/about')
def about():
    """
    :return: about page
    """
    return render_template('about.html', title='CFDB: About')

@punt.route('/')
@punt.route('/ncaa')
def ncaa():
    """
    :return: NCAA FBS page
    """
    conferences = [c for c in conf] # <---- this will need to change to a call to the database returning a list or generator of all the conferences
    return render_template('teams.html', confList=list(conferences), title='CFDB: NCAA')



# *********************************************************************************************************************
# Template API calls for populating website TABLE pages
# *********************************************************************************************************************

@punt.route('/')
@punt.route('/conf_table')
def conf_table():
    """
    :return: Conference table page
    """
    return render_template('conferenceTable.html', title='CFDB: Conference Table')


@punt.route('/')
@punt.route('/team_table')
def team_table():
    """
    :return: Team table page
    """
    return render_template('teamTable.html', title='CFDB: Team Table')

@punt.route('/')
@punt.route('/player_table')
def player_table():
    """
    :return: Player table page
    """
    return render_template('playerTable.html', title='CFDB: Player Table')


# *********************************************************************************************************************
# Template API calls for populating website PROFILE pages
# *********************************************************************************************************************


@punt.route('/')
@punt.route('/conf_t/<string:c_name>')
def conf_template(c_name):
    """
    :param c_name: the conference's name
    :return: the conference profile page populated with content specific for that conference
    """

    c = [c for c in conf if c['name'] == c_name] # <---- this will need to change to a call to the database returning all of the conference's attributes in a python dict MATCHING THE KEY NAMES INDICATED BELOW
    conference = c[0]
    return render_template('conference_profile.html', conf=conference['name'], year=conference['founded'], com=conference['comm'], champ=conference['champ'], num=conference['num_teams'], teamList=conference['teams'])



@punt.route('/')
@punt.route('/team_t/<string:t_name>')
def team_template(t_name):
    """
    :param t_name: the team's name
    :return: the team profile page populated with content specific for that team
    """
    t = [t for t in teams if t['name'] == t_name] # <---- this will need to change to a call to the database returning all of the team's attributes in a python dict MATCHING THE KEY NAMES INDICATED BELOW
    team = t[0]
    player_list = [player for player in players for p in team['roster'] if player['name'] == p]
    return render_template('team_profile.html', team=team['name'], conf=team['conf'], location=team['location'], coach=team['head_coach'], playerList=list(player_list), gameList=team['schedule'])


@punt.route('/')
@punt.route('/player_t/<string:p_name>')
def player_template(p_name):
    """
    :param p_name: the player's name
    :return: the player profile page populated with content specific for that player
    """
    p = [p for p in players if p['name'] == p_name] # <---- this will need to change to a call to the database returning all of the conference's attributes and a python dict MATCHING THE KEY NAMES INDICATED BELOW
    player = p[0]
    return render_template('player_profile.html', name=player['name'], number=player['no'], team=player['team'], year=player['year'], pos=player['pos'], ht=player['ht'], wt=player['wt'], town=player['hometown'], hs=player['hs'], photo=player['photo'])


if __name__ == '__main__':
    punt.run(debug=True, host='0.0.0.0')
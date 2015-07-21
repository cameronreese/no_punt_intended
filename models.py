#!/usr/bin/env python3

# -----------
# imports
# -----------
import json
import os
import requests
from urllib.request import urlopen
from random import randint
from flask import Flask, Request
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy
from subprocess import Popen, PIPE, check_output, STDOUT

punt = Flask(__name__)


punt.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:beard@localhost/cfdb_flask'
db = SQLAlchemy(punt)
# players model
class players(db.Model):
    id = db.Column(db.Integer,primary_key = True,unique = True,index = True)
    name = db.Column(db.String(256))
    no = db.Column(db.String(256))
    pos = db.Column(db.String(256))
    team = db.Column(db.String(256),db.ForeignKey('teams.name'))
    ht = db.Column(db.String(256))
    wt = db.Column(db.String(256))
    hometown = db.Column(db.String(256))
    year = db.Column(db.String(256))
    hs = db.Column(db.String(256))
    photo = db.Column(db.String(256))

    def __init__(self, id, name, no, pos, team, ht, wt, hometown, year, hs, photo):
        self.id = id
        self.name = name
        self.no = no
        self.pos = pos
        self.team = team
        self.ht = ht
        self.wt = wt
        self.hometown = hometown
        self.year = year
        self.hs = hs
        self.photo = photo

    def __iter__(self):
        yield self.id
        yield self.name
        yield self.no
        yield self.pos
        yield self.team
        yield self.ht
        yield self.wt
        yield self.hometown
        yield self.year
        yield self.hs
        yield self.photo


schedule = db.Table('schedule',db.Column('teams_name',db.String(256),db.ForeignKey('teams.name')),db.Column('game_id',db.Integer,db.ForeignKey('games.id')))
# teams model
class teams(db.Model):
    name = db.Column(db.String(256),primary_key = True)
    location = db.Column(db.String(256))
    roster = db.relationship('players')
    schedule = db.relationship('games',secondary=schedule)
    head_coach = db.Column(db.String(256))
    confname = db.Column(db.String(256),db.ForeignKey('conf.name'))

    def __init__(self, name, location, roster, head_coach, confname):
        self.name = name
        self.location = location
        self.roster = roster
        self.schedule = schedule
        self.head_coach = head_coach
        self.confname = confname

    def __iter__(self):
        yield self.name
        yield self.location
        yield list([p.name for p in self.roster])
        yield self.head_coach
        yield self.confname

# conference model
class conf(db.Model):
    name = db.Column(db.String(256),primary_key = True)
    founded = db.Column(db.String(256))
    champ = db.Column(db.String(256))
    teamset = db.relationship('teams')
    num_teams = db.Column(db.String(256))
    comm = db.Column(db.String(256))

    def __init__(self, name, founded, champ, teamset, num_teams, comm):
        self.name = name
        self.founded = founded
        self.champ = champ
        self.teamset = teamset
        self.num_teams = num_teams
        self.comm = comm

    def __iter__(self):
        yield self.name
        yield self.founded
        yield self.champ
        yield list([t.name for t in self.teamset])
        yield self.num_teams
        yield self.comm


# games model
class games(db.Model):
    id = db.Column(db.Integer,primary_key = True,unique = True,index = True)
    date = db.Column(db.String(256))
    home_team = db.Column(db.String(256),db.ForeignKey('teams.name'))
    away_team = db.Column(db.String(256),db.ForeignKey('teams.name'))
    location = db.Column(db.String(256))
    time = db.Column(db.String(256))


# *********************************************************************************************************************
# API calls to retrieve model specific data
# *********************************************************************************************************************


@punt.route('/punt/players/<string:player_name>', methods=['GET'])
def get_players(player_name):
    """ GET method
        takes in a player's name as an argument from an http URL
        and returns data object of the players attributes
        to retrieve info for all players use 'players' as input
    """
    qryresult = players.query.get(player_name)
    result = ""
    _it = iter(qryresult)
    result = "{\n\t\"id\": \"" + str(next(_it)) + "\",\n\t\"name\": \"" + next(_it) + "\",\n\t\"no\": \"" + next(_it) + "\",\n\t\"pos\": \"" + next(_it) + "\",\n\t\"team\" : \"" + next(_it) + "\",\n\t\"ht\": \"" + next(_it) + "\",\n\t\"wt\": \"" + next(_it) + "\",\n\t\"hometown\": \"" + next(_it) + "\",\n\t\"year\": \"" + next(_it) + "\",\n\t\"hs\": \"" + next(_it) + "\",\n\t\"photo\": \"" + next(_it) + "\"\n}"
    return result

@punt.route('/punt/teams/<string:team_name>', methods=['GET'])
def get_teams(team_name):
    """ GET method
        takes in a team's name as an argument from an http URL
        and returns json object of the team's attributes
        to retrieve info for all teams use 'teams' as input
    """
    qryresult = teams.query.get(team_name)
    result = ""
    _it = iter(qryresult)
    result = "{\n\t\"name\": \"" + next(_it) + "\"" + ",\n\t\"location\": \"" + next(_it) + "\",\n\t\"roster\": ["
    roster_list = next(_it)
    for p in roster_list:
        result += ("\"" + p + "\", ")
    result = result[:-2]
    result += "],\n\t\"head_coach\": \"" + next(_it) + "\",\n\t\"confname\": \"" + next(_it) + "\"\n}"
    return result

@punt.route('/punt/conf/<string:conf_name>', methods=['GET'])
def get_conf(conf_name):
    """ GET method
        takes in a conference's nickname as an argument from an http URL
        and returns json object of the conference's attributes
        to retrieve info for all conferences use 'conf' as input
    """
    qryresult = conf.query.get(conf_name)
    result = ""
    _it = iter(qryresult)
    result = "{\n\t\"name\": \"" + next(_it) + "\"" + ",\n\t\"founded\": " + "\"" + next(_it) + "\",\n\t\"champ\": \"" + next(_it) + "\",\n\t\"teamset\": ["
    team_list = next(_it)
    for t in team_list:
        result += ("\"" + t + "\", ")
    result = result[:-2]
    result += "],\n\t\"num_teams\": \"" + next(_it) + "\",\n\t\"comm\": \"" + next(_it) + "\"\n}"
    return result


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
    conferences = conf.query.all()
    return render_template('teams.html', confList=list(conferences) , title='CFDB: NCAA')


# *********************************************************************************************************************
# Template API calls for populating website TABLE pages
# *********************************************************************************************************************

@punt.route('/')
@punt.route('/conf_table')
def conf_table():
    """
    :return: Conference table page
    """
    conference_list = conf.query.all()
    return render_template('conferenceTable.html', confList=list(conference_list), title='CFDB: Conference Table')


@punt.route('/')
@punt.route('/team_table')
def team_table():
    """
    :return: Team table page
    """
    team_list = teams.query.all()
    return render_template('teamTable.html', teamList=list(team_list), title='CFDB: Team Table')

@punt.route('/')
@punt.route('/player_table')
def player_table():
    """
    :return: Player table page
    """
    player_list = players.query.all()
    return render_template('playerTable.html', playerList=list(player_list), title='CFDB: Player Table')


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
    conference = conf.query.get(c_name)
    team_list = [t.name for t in conference.teamset]
    return render_template('conference_profile.html', conf=conference.name, year=conference.founded, com=conference.comm, champ=conference.champ, num=conference.num_teams, teamList=list(team_list))



@punt.route('/')
@punt.route('/team_t/<string:t_name>')
def team_template(t_name):
    """
    :param t_name: the team's name
    :return: the team profile page populated with content specific for that team
    """
    team = teams.query.get(t_name)
    player_list = [p for p in team.roster]
    game_list = [g for g in team.schedule]
    return render_template('team_profile.html', team=team.name, conf=team.confname, location=team.location, coach=team.head_coach, playerList=list(player_list), gameList=list(game_list))

@punt.route('/')
@punt.route('/player_t/<string:p_id>')
def player_template(p_id):
    """
    :param p_name: the player's name
    :return: the player profile page populated with content specific for that player
    """
    p = players.query.get(p_id)
    return render_template('player_profile.html', player=p)

# *********************************************************************************************************************
# Template API calls for populating website using other team's project API
# *********************************************************************************************************************

@punt.route('/')
@punt.route('/api2k15')
def api2k15():
    """
    : return: renders the page that we use the other project's API
    """
    player_id = str(randint(1, 446))
    response = requests.get('http://api2k15.me/resources/player/' + player_id)
    player_data = response.json()

    false1_id = str(randint(1, 446))
    response = requests.get('http://api2k15.me/resources/player/' + false1_id)
    false1_data = response.json()

    while false1_data['team_name'] == player_data['team_name']:
        false1_id = str(randint(1, 446))
        response = requests.get('http://api2k15.me/resources/player/' + false1_id)
        false1_data = response.json()

    false2_id = str(randint(1, 446))
    response = requests.get('http://api2k15.me/resources/player/' + false2_id)
    false2_data = response.json()

    while false2_data['team_name'] == player_data['team_name']:
        false2_id = str(randint(1, 446))
        response = requests.get('http://api2k15.me/resources/player/' + false2_id)
        false2_data = response.json()

    return render_template('api2k15.html', photo=player_data['picture'], player_team=player_data['team_name'], false1=false1_data['team_name'], false2=false2_data['team_name'])



@punt.route('/')
@punt.route('/unittest')
def unittest():
    """
    :return: renders the page that displays the results of the unittests
    """
    w_out = open('result.txt', 'r+')
    Popen("python3 -m unittest -v tests.py", shell=True, stdout=w_out, stderr=STDOUT)
    w_out.close()
    with open('result.txt', 'r') as result_file:
        result_output = result_file.readlines()
    result_file.close()
    return render_template('test_result.html', result=result_output)

    # res = check_output(["tests.py"])
    # return render_template('test_result.html', result=res)


@punt.route('/')
@punt.route('/search')
def copaDB():
    """
    : return: renders the page that we use for the search results
    """
    return render_template('search.html')


if __name__ == '__main__':
    punt.run(debug=True, host='0.0.0.0')

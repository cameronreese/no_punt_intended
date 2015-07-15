#!/usr/bin/env python3

# -----------
# imports
# -----------

from flask import Flask
from flask import jsonify
from flask import abort
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy



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
#schedule = db.Table('schedule',db.Column('teams_name',db.String(256),db.ForeignKey('teams.name')),db.Column('game_id',db.Integer,db.ForeignKey('games.id')))
# teams model
class teams(db.Model):
    name = db.Column(db.String(256),primary_key = True)
    location = db.Column(db.String(256))
    roster = db.relationship('players')
    #schedule = db.relationship('games',secondary=schedule,backref=db.backref('teams',lazy='dynamic'))
    head_coach = db.Column(db.String(256))
    confname = db.Column(db.String(256),db.ForeignKey('conf.name'))
# conference model
class conf(db.Model):
    name = db.Column(db.String(256),primary_key = True)
    founded = db.Column(db.String(256))
    champ = db.Column(db.String(256))
    teamset = db.relationship('teams')
    num_teams = db.Column(db.String(256))
    comm = db.Column(db.String(256))
# games model
# class games(db.Model):
#     id = db.Column(db.Integer,primary_key = True,unique = True,index = True)
#     date = db.Column(db.String(256))
#     home_team = db.Column(db.String(256),db.ForeignKey('teams.name'))
#     away_team = db.Column(db.String(256),db.ForeignKey('teams.name'))
#     location = db.Column(db.String(256),db.ForeignKey('teams.location'))
#     time = db.Column(db.String(256))


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
    if player_name == 'players':
        return players.query.all()
    else:
        return players.query.get(player_name)

@punt.route('/punt/teams/<string:team_name>', methods=['GET'])
def get_teams(team_name):
    """ GET method
        takes in a team's name as an argument from an http URL 
        and returns json object of the team's attributes 
        to retrieve info for all teams use 'teams' as input
    """
    if team_name == 'teams':
        return teams.query.all()
    else:
        return teams.query.get(team_name)

@punt.route('/punt/conf/<string:conf_name>', methods=['GET'])
def get_conf(conf_name):
    """ GET method
        takes in a conference's nickname as an argument from an http URL 
        and returns json object of the conference's attributes
        to retrieve info for all conferences use 'conf' as input
    """
    if conf_name == 'conf':
        return conf.query.all()
    else:
        return conf.query.get(conf_name)


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
    return render_template('team_profile.html', team=team.name, conf=team.confname, location=team.location, coach=team.head_coach, playerList=list(player_list))
# gameList=team['schedule'] <---- add schedule back in

@punt.route('/')
@punt.route('/player_t/<string:p_id>')
def player_template(p_id):
    """
    :param p_name: the player's name
    :return: the player profile page populated with content specific for that player
    """
    p = players.query.get(p_id)
    return render_template('player_profile.html', player=p)
#name=player.name, number=player.no, team=player.team, year=player.year, pos=player.pos, ht=player.ht, wt=player.wt, town=player.hometown, hs=player.hs, photo=player.photo

if __name__ == '__main__':
    punt.run(debug=True, host='0.0.0.0')

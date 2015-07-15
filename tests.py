#!/usr/bin/env python3

# -----------
# imports
# -----------
from io     import StringIO
from unittest import main, TestCase
from urllib.request import urlopen
import json
import requests

from flask import Flask, Response
from flask import jsonify
from flask import abort

# -----------
# TestModels
# -----------

class TestModels(TestCase):

    # -----------
    # get_players
    # -----------
    def test_get_players_1(self):
        player = {"players": {"hometown": "Coppell, TX", "no": "#28", "ht": "6-1", "pos": "PK", "team": "Texas Longhorns", "name": "Nick Jordan", "wt": "193"}}
        data = requests.get('http://cfdb.me:5000/punt/players/Nick%20Jordan').json()
        print(data)
        #self.assertEqual(player, data)

    def test_get_players_2(self):
        player = {'players': {'hometown': 'Shreveport, LA', 'ht': '6-3', 'team': 'Texas Longhorns', 'pos': 'DE', 'name': 'Shiro Davis', 'wt': '265', 'no': '#1'}}
        data = requests.get('http://cfdb.me:5000/punt/players/Shiro%20Davis').json()
        #self.assertEqual(player, data)

    def test_get_players_3(self):
        player = {'players': {'hometown': 'San Antonio, TX', 'ht': '5-10', 'team': 'Baylor Bears', 'pos': 'LB', 'name': 'Jeff Bryson', 'wt': '200', 'no': '#59'}}
        data = requests.get('http://cfdb.me:5000/punt/players/Jeff%20Bryson').json()
        #self.assertEqual(player, data)

    # -----------
    # get_teams
    # -----------
    def test_get_teams_1(self):
        team = {'teams': {'roster': ['Nick Jordan', 'Shiro Davis'], 'conf': 'Big 12', 'schedule': [], 'name': 'Texas Longhorns', 'location': 'Austin, TX', 'head_coach': 'Charlie Strong'}}
        data = requests.get('http://cfdb.me:5000/punt/teams/Texas%20Longhorns').json()
        print(data)
        #self.assertEqual(team, data)

    def test_get_teams_2(self):
        team = {"teams": {"name": "Baylor Bears"}}
        data = requests.get('http://cfdb.me:5000/punt/teams/Baylor%20Bears').json()
        #self.assertEqual(team, data)

    def test_get_teams_3(self):
        team = {"teams": {"name": "TCU Horned Frogs"}}
        data = requests.get('http://cfdb.me:5000/punt/teams/TCU%20Horned%20Frogs').json()
        #self.assertEqual(team, data)

    # -----------
    # get_conf
    # -----------
    def test_get_conf_1(self):
        conf = {'conf': {'teams': [], 'name': 'Big 12', 'founded': 'some year', 'number_of_teams': 'a_num', 'current_conf_champion': 'team'}}
        data = requests.get('http://cfdb.me:5000/punt/conf/Big%2012').json()
        print(data)
        #self.assertEqual(conf, data)

    def test_get_conf_2(self):
        conf = {"conf": {"name": "Big Ten"}}
        data = requests.get('http://cfdb.me:5000/punt/conf/Big%20Ten').json()
        #self.assertEqual(conf, data)

    def test_get_conf_3(self):
        conf = {"conf": {"name": "ACC"}}
        data = requests.get('http://cfdb.me:5000/punt/conf/ACC').json()
        #self.assertEqual(conf, data)
# ----
# main
# ----

if __name__ == "__main__":
    main()

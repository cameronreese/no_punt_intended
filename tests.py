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
from models import get_players, get_teams, get_conf

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
        self.assertEqual(player, data)

    def test_get_players_2(self):
        player = {
            'name': 'Shiro Davis',
            'no': '#1',
            'pos': 'DE',
            'team': 'Texas Longhorns',
            'ht': '6-3',
            'wt': '265',
            'hometown': 'Shreveport, LA',
        }
        data = requests.get('http://cfdb.me:5000/punt/players/Shiro%20Davis').json()
        self.assertEqual(player, data)

    def test_get_players_3(self):
        player = {
            'name': 'Jeff Bryson',
            'no': '#59',
            'pos': 'LB',
            'team': 'Baylor Bears',
            'ht': '5-10',
            'wt': '200',
            'hometown': 'San Antonio, TX',
        }
        data = requests.get('http://cfdb.me:5000/punt/players/Jeff%20Bryson').json()
        self.assertEqual(player, data)


# ----
# main
# ----

if __name__ == "__main__":
    main()

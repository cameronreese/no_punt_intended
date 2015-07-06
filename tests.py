#!/usr/bin/env python3

# -----------
# imports
# -----------
from io     import StringIO
from unittest import main, TestCase
from urllib.request import urlopen
import json

from flask import Flask
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
        player = {
            'name': 'Nick Jordan',
            'no': '#28',
            'pos': 'PK',
            'team': 'Texas Longhorns',
            'ht': '6-1',
            'wt': '193',
            'hometown': 'Coppell, TX',
        }
        data = urlopen('http://cfdb.me/punt/Nick%20Jordan')
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
        data = urlopen('http://cfdb.me/punt/Shiro%20Davis')
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
        data = urlopen('http://cfdb.me/punt/Jeff%20Bryson')
        self.assertEqual(player, data)


# ----
# main
# ----

if __name__ == "__main__":
    main()

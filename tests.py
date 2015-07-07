#!/usr/bin/env python3

# -----------
# imports
# -----------
from io     import StringIO
from unittest import main, TestCase
from urllib.request import urlopen
import json

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
        player = {
            'name': 'Nick Jordan',
            'no': '#28',
            'pos': 'PK',
            'team': 'Texas Longhorns',
            'ht': '6-1',
            'wt': '193',
            'hometown': 'Coppell, TX',
        }
        response = urlopen('http://cfdb.me:5000/punt/players/Nick%20Jordan')
        data = json.loads(response)
        # v = data[players]
        print(data)
        #self.assertEqual(player, v)

    # def test_get_players_2(self):
    #     player = {
    #         'name': 'Shiro Davis',
    #         'no': '#1',
    #         'pos': 'DE',
    #         'team': 'Texas Longhorns',
    #         'ht': '6-3',
    #         'wt': '265',
    #         'hometown': 'Shreveport, LA',
    #     }
    #     response = urlopen('http://cfdb.me:5000/punt/players/Jeff%20Bryson')
    #     data = json.load(response)
    #     v = data[players]
    #     print(v)
    #     #self.assertEqual(player, v)
    #
    # def test_get_players_3(self):
    #     player = {
    #         'name': 'Jeff Bryson',
    #         'no': '#59',
    #         'pos': 'LB',
    #         'team': 'Baylor Bears',
    #         'ht': '5-10',
    #         'wt': '200',
    #         'hometown': 'San Antonio, TX',
    #     }
    #     response = urlopen('http://cfdb.me:5000/punt/players/Jeff%20Bryson')
    #     data = json.load(response)
    #     v = data[players]
    #     print(v)
        #self.assertEqual(player, v)


# ----
# main
# ----

if __name__ == "__main__":
    main()

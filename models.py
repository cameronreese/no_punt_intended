#!/usr/bin/env python3

# -----------
# imports
# -----------
import random
from numpy import mean, sqrt, square, subtract
import json

from flask import Flask

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
        'schedule': {}, # a dict of {date : opponent}
    },
        {
        'name': 'Baylor Bears',
        'location': 'Waco, TX',
        'roster': (), # tuple of player links
        'schedule': {}, # a dict of {date : opponent}
    },
        {
        'name': 'TCU Horned Frogs',
        'location': 'Fort Worth, TX',
        'roster': (), # tuple of player links
        'schedule': {}, # a dict of {date : opponent}
    }
]

''' leaving coaches out for now since I can not seem to find any info on them easily '''
# coaches = [
#     {
#
#     }
# ]

@punt.route('/api')
def get_players():
    return jsonify({'players': players})

def get_teams():
    return jsonify({'teams': teams})

if __name__ == '__main__':
    punt.run(debug=True)

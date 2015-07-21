#!/usr/bin/env python3

# -----------
# imports
# -----------
from unittest import main, TestCase
from urllib.request import urlopen
import json


# -----------
# TestModels
# -----------

class TestModels(TestCase):

    # -----------
    # get_players
    # -----------
    def test_get_players_1(self):
        player = {
                    "id": "10111",
                    "name": "Austin Stewart",
                    "no": "8",
                    "pos": "DB",
                    "team" : "Texas Tech",
                    "ht": "-",
                    "wt": "223",
                    "hometown": "Matthews, NC",
                    "year": "SR",
                    "hs": "Pierce College",
                    "photo": ""
                  }
        url = urlopen('http://cfdb.me:5000/punt/players/10111')
        data = url.read().decode(url.info().get_param('charset') or 'utf-8')
        d = json.loads(data)
        self.assertEqual(d['id'], player['id'])

    def test_get_players_2(self):
        player = {
                    "id": "8041",
                    "name": "Phillip Dorsett",
                    "no": "4",
                    "pos": "WR",
                    "team" : "Miami",
                    "ht": "5-10",
                    "wt": "195",
                    "hometown": "Ft Lauderdale, FL",
                    "year": "SR",
                    "hs": "St Thomas Aquinas HS",
                    "photo": "http://sports.cbsimg.net/images/collegefootball/players/60x80/1836058.jpg"
                 }
        url = urlopen('http://cfdb.me:5000/punt/players/8041')
        data = url.read().decode(url.info().get_param('charset') or 'utf-8')
        d = json.loads(data)
        self.assertEqual(d['id'], player['id'])

    def test_get_players_3(self):
        player = {
                    "id": "8038",
                    "name": "Trevor Darling",
                    "no": "73",
                    "pos": "OL",
                    "team" : "Miami",
                    "ht": "6-5",
                    "wt": "310",
                    "hometown": "Miami, FL",
                    "year": "FR",
                    "hs": "Miami Central HS",
                    "photo": ""
                 }
        url = urlopen('http://cfdb.me:5000/punt/players/8038')
        data = url.read().decode(url.info().get_param('charset') or 'utf-8')
        d = json.loads(data)
        self.assertEqual(d['id'], player['id'])

    def test_get_players_4(self):
        player = {
                    "id": "10111",
                    "name": "Austin Stewart",
                    "no": "8",
                    "pos": "DB",
                    "team" : "Texas Tech",
                    "ht": "-",
                    "wt": "223",
                    "hometown": "Matthews, NC",
                    "year": "SR",
                    "hs": "Pierce College",
                    "photo": ""
                  }
        url = urlopen('http://cfdb.me:5000/punt/players/10111')
        data = url.read().decode(url.info().get_param('charset') or 'utf-8')
        d = json.loads(data)
        self.assertEqual(d['hometown'], player['hometown'])

    def test_get_players_5(self):
        player = {
                    "id": "8041",
                    "name": "Phillip Dorsett",
                    "no": "4",
                    "pos": "WR",
                    "team" : "Miami",
                    "ht": "5-10",
                    "wt": "195",
                    "hometown": "Ft Lauderdale, FL",
                    "year": "SR",
                    "hs": "St Thomas Aquinas HS",
                    "photo": "http://sports.cbsimg.net/images/collegefootball/players/60x80/1836058.jpg"
                 }
        url = urlopen('http://cfdb.me:5000/punt/players/8041')
        data = url.read().decode(url.info().get_param('charset') or 'utf-8')
        d = json.loads(data)
        self.assertEqual(d['hometown'], player['hometown'])

    def test_get_players_6(self):
        player = {
                    "id": "8038",
                    "name": "Trevor Darling",
                    "no": "73",
                    "pos": "OL",
                    "team" : "Miami",
                    "ht": "6-5",
                    "wt": "310",
                    "hometown": "Miami, FL",
                    "year": "FR",
                    "hs": "Miami Central HS",
                    "photo": ""
                 }
        url = urlopen('http://cfdb.me:5000/punt/players/8038')
        data = url.read().decode(url.info().get_param('charset') or 'utf-8')
        d = json.loads(data)
        self.assertEqual(d['wt'], player['wt'])

    def test_get_players_7(self):
        player = {
                    "id": "10111",
                    "name": "Austin Stewart",
                    "no": "8",
                    "pos": "DB",
                    "team" : "Texas Tech",
                    "ht": "-",
                    "wt": "223",
                    "hometown": "Matthews, NC",
                    "year": "SR",
                    "hs": "Pierce College",
                    "photo": ""
                  }
        url = urlopen('http://cfdb.me:5000/punt/players/10111')
        data = url.read().decode(url.info().get_param('charset') or 'utf-8')
        d = json.loads(data)
        self.assertEqual(d['name'], player['name'])

    def test_get_players_8(self):
        player = {
                    "id": "8041",
                    "name": "Phillip Dorsett",
                    "no": "4",
                    "pos": "WR",
                    "team" : "Miami",
                    "ht": "5-10",
                    "wt": "195",
                    "hometown": "Ft Lauderdale, FL",
                    "year": "SR",
                    "hs": "St Thomas Aquinas HS",
                    "photo": "http://sports.cbsimg.net/images/collegefootball/players/60x80/1836058.jpg"
                 }
        url = urlopen('http://cfdb.me:5000/punt/players/8041')
        data = url.read().decode(url.info().get_param('charset') or 'utf-8')
        d = json.loads(data)
        self.assertEqual(d['team'], player['team'])

    def test_get_players_9(self):
        player = {
                    "id": "8038",
                    "name": "Trevor Darling",
                    "no": "73",
                    "pos": "OL",
                    "team" : "Miami",
                    "ht": "6-5",
                    "wt": "310",
                    "hometown": "Miami, FL",
                    "year": "FR",
                    "hs": "Miami Central HS",
                    "photo": ""
                 }
        url = urlopen('http://cfdb.me:5000/punt/players/8038')
        data = url.read().decode(url.info().get_param('charset') or 'utf-8')
        d = json.loads(data)
        self.assertEqual(d['hs'], player['hs'])

    # -----------
    # get_teams
    # -----------
    def test_get_teams_1(self):
        team = {
                    'name': 'Texas',
                    'location': 'Austin',
                    'roster': ['Eddie Aboussie', 'Brandon Allen', 'Alex Anderson', 'David Ash', 'Kyle Ashby', 'Andrew Beck', 'Mitchell Becker', 'Roderick Bernard', 'Caleb Bluiett', 'Dillon Boldt', 'John Bonney', 'Cody Boswell', 'Nate Boyer', 'Paul Boyette Jr', 'Malcolm Brown', 'Malcom Brown', 'Donald Catalon', 'Matt Center', 'Demarco Cobbs', 'Adrian Colbert', 'Timothy Cole', 'Bryce Cottrell', 'Dominic Cruciani', 'Terrell Cuney', 'Greg Daniels', 'Michael Davidson', 'Antwuan Davis', 'Deoundrei Davis', 'Gaston Davis', 'Shiro Davis', 'Alex De La Torre', 'Hunter DeGroot', 'Quandre Diggs', 'Taylor Doyle', 'Bryson Echols', 'Steve Edmond', 'Dominic Espinosa', 'Kennedy Estelle', 'Sheroid Evans', 'Sedrick Flowers', 'Poona Ford', 'Armanti Foreman', 'DOnta Foreman', 'Edwin Freeman', 'Dererick Giles', 'Chris Giron', 'Trey Gonzales', 'Garrett Graf', 'Garrett Gray', 'Johnathan Gray', 'Jimmy Greenwood', 'Trenton Hafley', 'Dakota Haines', 'Dylan Haines', 'Jason Hall', 'Cameron Hampton', 'John Harris', 'Desmond Harrison', 'Jerrod Heard', 'Jordan Hicks', 'Jak Holbrook', 'Trey Holtz', 'Devin Huffines', 'Connor Huffman', 'Camrhon Hughes', 'Naashon Hughes', 'Erik Huhn', 'Marcus Hutchins', 'Desmond Jackson', 'Tevin Jackson', 'Darius James', 'Peter Jinkens', 'Lorenzo Joe', 'Daje Johnson', 'Marcus Johnson', 'Nick Jordan', 'Nick Kreider', 'Tyler Lee', 'Dorian Leonard', 'Frank Lopez', 'Tyler Marriott', 'MJ McFarland', 'Jake McMillon', 'Alex Mercado', 'Logan Mills', 'Chris Nelson', 'Alex Norman', 'Jake Oliver', 'Miles Onyegbule', 'Clark Orren', 'Kent Perkins', 'Ben Pruitt', 'Jake Raulerson', 'Cedric Reed', 'Hassan Ridgeway', 'Curtis Riser', 'Derick Roberson', 'Ryan Roberts', 'Jermaine Roberts Jr', 'Daniel Rodriguez', 'Elijah Rodriguez', 'Nick Rose', 'William Russ', 'Dalton Santos', 'Jaxon Shipley', 'Matthew Sims', 'Jordan Strickland', 'Geoff Swaim', 'Tyrone Swoopes', 'Ty Templin', 'Chris Terry', 'David Thomann', 'Duke Thomas', 'Mykkele Thompson', 'Johnny Tseng', 'Josh Turner', 'Kevin Vaccaro', 'Logan Vinklarek', 'Jacorey Warrick', 'Michael Welsh', 'Blake Whiteley', 'Michael Wilson'],
                    'head_coach': 'Charlie Strong',
                    'confname': 'Big 12'
                }
        url = urlopen('http://cfdb.me:5000/punt/teams/Texas')
        data = url.read().decode(url.info().get_param('charset') or 'utf-8')
        d = json.loads(data)
        self.assertEqual(d['name'], team['name'])

    def test_get_teams_2(self):
        team = {
                    'name': 'Baylor',
                    'location': 'Waco',
                    'roster': ['TreVon Armstead', 'Troy Baker', 'Andrew Billings', 'Baylor Black', 'Blake Blackmar', 'Beau Blackshear', 'Jourdan Blake', 'Travon Blanchard', 'Byron Bonds', 'Collin Brence', 'Lee Bristow', 'Terell Brooks', 'Brandon Brown', 'Jarell Broxton', 'Terrell Burt', 'Chris Callahan', 'Grant Campbell', 'KD Cannon', 'Devin Chafin', 'Trevor Clemons-Valdez', 'Pat Colbert', 'Corey Coleman', 'Raaquan Davis', 'Cordell Dorsey', 'Spencer Drango', 'Drew Earnest', 'Cole Edmiston', 'Aiavion Edwards', 'Tyler Edwards', 'Nelson Ehirim', 'Kendall Ehrlich', 'Spencer Evans', 'Jordan Feuerbacher', 'Mallory Franklin', 'Andrew Frerking', 'Clay Fuller', 'Kyle Fuller', 'Antwan Goodley', 'Bryce Hager', 'Davion Hall', 'Rami Hammad', 'Lynx Hawthorne', 'Calvin Hill', 'Desmine Hilliard', 'Xavien Howard', 'Iain Hunter', 'Jamie Jacobs', 'Tyler Jaynes', 'Johnny Jefferson', 'Chris Johnson', 'Miles Johnson', 'Quan Jones', 'Xavier Jones', 'BJ Jordan', 'Jarrod Koym', 'Jimmy Landes', 'Patrick Lawrence', 'Jay Lee', 'Patrick Levels', 'Ira Lewis', 'Shock Linwood', 'Javonte Magee', 'Blake Mahon', 'Josh Malin', 'Suleiman Masumbuko', 'LaQuan McGowan', 'Kevin Mitchell', 'Kaleb Moore', 'Andrew Morris', 'Blake Muir', 'Sean Muir', 'Silas Nacita', 'Brian Nance', 'Levi Norwood', 'Shawn Oakman', 'Keith Orcutt', 'Jason Osei', 'Jamal Palmer', 'Josh Pelzel', 'Gus Penning', 'Kyle Peterson', 'Bryce Petty', 'Xavier Phillips', 'Chris Platt', 'Alfred Pullom', 'Ryan Reid', 'Tanner Ritchey', 'Andy Ritter', 'Greg Roberts', 'Spencer Roth', 'Seth Russell', 'Chris Sanders', 'Taion Sells', 'Collin Simpson', 'Terrence Singleton', 'KJ Smith', 'Cal Spangler', 'Orion Stewart', 'Tanner Thrift', 'Verkedric Vaughns', 'Chance Waz', 'Anthony Webb', 'Trevor White', 'Terence Williams', 'Ishmael Wilson', 'Tion Wright', 'Taylor Young', 'Ishmael Zamora'],
                    'head_coach': 'Art Briles',
                    'confname': 'Big 12'
                }
        url = urlopen('http://cfdb.me:5000/punt/teams/Baylor')
        data = url.read().decode(url.info().get_param('charset') or 'utf-8')
        d = json.loads(data)
        self.assertEqual(d['name'], team['name'])

    def test_get_teams_3(self):
        team = {
                    'name': 'TCU',
                    'location': 'Fort Worth',
                    'roster': ['Zach Allen', 'Garrett Altman', 'Demetrion Amie', 'Jonathan Anderson', 'Philip Armendarez', 'Femi Awe', 'George Baltimore', 'Ty Barrett', 'Luke Benuska', 'Matt Boggs', 'Stacy Boyd', 'Trevone Boykin', 'Chris Bradley', 'Bryson Burtnett', 'Cyd Calvin', 'Justus Canfield', 'Josh Carraway', 'Sam Carter', 'BJ Catalon', 'Chad Childs', 'Colten Christensen', 'LJ Collier', 'Aviante Collins', 'George Cullen', 'Aaron Curry', 'Paul Dawson', 'Ryan DeNucci', 'Josh Doctson', 'Sammy Douglas', 'Michael Downing', 'Keaton Duhon', 'Cameron Echols-Luper', 'Trey Elliott', 'Tayo Fabuluje', 'Brady Foltz', 'Travoskey Garrett', 'Griffin Gilbert', 'Deante Gray', 'Aaron Green', 'Kolby Griffin', 'Ryan Griswold', 'Chris Hackett', 'Travis Hanes', 'Bryson Henderson', 'Blake Henningsen', 'Nathan Hernandez', 'Kyle Hicks', 'Geoff Hooker', 'Travin Howard', 'Joey Hunt', 'Chucky Hunter', 'Kenny Iloka', 'Ridwan Issahaku', 'Matt Joeckel', 'Denzel Johnson', 'Trevorris Johnson', 'Buck Jones', 'Garrett Kaufman', 'Frank Kee', 'Devin Killpatrick', 'Derrick Kindred', 'Bram Kohlhausen', 'Terrell Lathan', 'Tevin Lawson', 'Robert Lewis', 'Kolby Listenbee', 'Michael MacCrory', 'Marcus Mallet', 'Corey McBride', 'Casey McDermott Vai', 'James McFarland', 'Dominic Merka', 'Preston Miller', 'Jordan Moore', 'Patrick Morris', 'Ian Moser', 'Michael Mosharrafa', 'Torrance Mosley', 'Grayson Muehlstein', 'Cliff Murphy', 'Jamelle Naff', 'Shaun Nixon', 'Joseph Noteboom', 'Cole Novak', 'Corry OMeally', 'Jaden Oberkrom', 'Peter Okonofua', 'Nick Orr', 'Connor Osborne', 'Rahmaan Patterson', 'Ethan Perry', 'Keaton Perry', 'Andre Petties-Wilson', 'Davion Pierson', 'David Porter', 'Emanuel Porter', 'James Power', 'Matt Pryor', 'Charlie Reid', 'Foster Sawyer', 'Austin Schlottman', 'Ty Slanina', 'JaJuan Story', 'Ty Summers', 'Phil Taylor', 'Ranthony Texada', 'Bobby Thompson', 'Mike Tuaua', 'Lloyd Tunstill', 'Halapoulivaati Vaitai', 'Daniel Walsh', 'Thomas Walsh', 'Steve Wesley', 'Desmon White', 'Kevin White', 'Paul Whitmill', 'Russell Williams', 'Patrick Zeller'],
                    'head_coach': 'Gary Patterson',
                    'confname': 'Big 12'
                }
        url = urlopen('http://cfdb.me:5000/punt/teams/TCU')
        data = url.read().decode(url.info().get_param('charset') or 'utf-8')
        d = json.loads(data)
        self.assertEqual(d['name'], team['name'])

    def test_get_teams_4(self):
        team = {
                    'name': 'TCU',
                    'location': 'Fort Worth',
                    'roster': ['Zach Allen', 'Garrett Altman', 'Demetrion Amie', 'Jonathan Anderson', 'Philip Armendarez', 'Femi Awe', 'George Baltimore', 'Ty Barrett', 'Luke Benuska', 'Matt Boggs', 'Stacy Boyd', 'Trevone Boykin', 'Chris Bradley', 'Bryson Burtnett', 'Cyd Calvin', 'Justus Canfield', 'Josh Carraway', 'Sam Carter', 'BJ Catalon', 'Chad Childs', 'Colten Christensen', 'LJ Collier', 'Aviante Collins', 'George Cullen', 'Aaron Curry', 'Paul Dawson', 'Ryan DeNucci', 'Josh Doctson', 'Sammy Douglas', 'Michael Downing', 'Keaton Duhon', 'Cameron Echols-Luper', 'Trey Elliott', 'Tayo Fabuluje', 'Brady Foltz', 'Travoskey Garrett', 'Griffin Gilbert', 'Deante Gray', 'Aaron Green', 'Kolby Griffin', 'Ryan Griswold', 'Chris Hackett', 'Travis Hanes', 'Bryson Henderson', 'Blake Henningsen', 'Nathan Hernandez', 'Kyle Hicks', 'Geoff Hooker', 'Travin Howard', 'Joey Hunt', 'Chucky Hunter', 'Kenny Iloka', 'Ridwan Issahaku', 'Matt Joeckel', 'Denzel Johnson', 'Trevorris Johnson', 'Buck Jones', 'Garrett Kaufman', 'Frank Kee', 'Devin Killpatrick', 'Derrick Kindred', 'Bram Kohlhausen', 'Terrell Lathan', 'Tevin Lawson', 'Robert Lewis', 'Kolby Listenbee', 'Michael MacCrory', 'Marcus Mallet', 'Corey McBride', 'Casey McDermott Vai', 'James McFarland', 'Dominic Merka', 'Preston Miller', 'Jordan Moore', 'Patrick Morris', 'Ian Moser', 'Michael Mosharrafa', 'Torrance Mosley', 'Grayson Muehlstein', 'Cliff Murphy', 'Jamelle Naff', 'Shaun Nixon', 'Joseph Noteboom', 'Cole Novak', 'Corry OMeally', 'Jaden Oberkrom', 'Peter Okonofua', 'Nick Orr', 'Connor Osborne', 'Rahmaan Patterson', 'Ethan Perry', 'Keaton Perry', 'Andre Petties-Wilson', 'Davion Pierson', 'David Porter', 'Emanuel Porter', 'James Power', 'Matt Pryor', 'Charlie Reid', 'Foster Sawyer', 'Austin Schlottman', 'Ty Slanina', 'JaJuan Story', 'Ty Summers', 'Phil Taylor', 'Ranthony Texada', 'Bobby Thompson', 'Mike Tuaua', 'Lloyd Tunstill', 'Halapoulivaati Vaitai', 'Daniel Walsh', 'Thomas Walsh', 'Steve Wesley', 'Desmon White', 'Kevin White', 'Paul Whitmill', 'Russell Williams', 'Patrick Zeller'],
                    'head_coach': 'Gary Patterson',
                    'confname': 'Big 12'
                }
        url = urlopen('http://cfdb.me:5000/punt/teams/TCU')
        data = url.read().decode(url.info().get_param('charset') or 'utf-8')
        d = json.loads(data)
        self.assertEqual(d['location'], team['location'])

    def test_get_teams_5(self):
        team = {
                    'name': 'Baylor',
                    'location': 'Waco',
                    'roster': ['TreVon Armstead', 'Troy Baker', 'Andrew Billings', 'Baylor Black', 'Blake Blackmar', 'Beau Blackshear', 'Jourdan Blake', 'Travon Blanchard', 'Byron Bonds', 'Collin Brence', 'Lee Bristow', 'Terell Brooks', 'Brandon Brown', 'Jarell Broxton', 'Terrell Burt', 'Chris Callahan', 'Grant Campbell', 'KD Cannon', 'Devin Chafin', 'Trevor Clemons-Valdez', 'Pat Colbert', 'Corey Coleman', 'Raaquan Davis', 'Cordell Dorsey', 'Spencer Drango', 'Drew Earnest', 'Cole Edmiston', 'Aiavion Edwards', 'Tyler Edwards', 'Nelson Ehirim', 'Kendall Ehrlich', 'Spencer Evans', 'Jordan Feuerbacher', 'Mallory Franklin', 'Andrew Frerking', 'Clay Fuller', 'Kyle Fuller', 'Antwan Goodley', 'Bryce Hager', 'Davion Hall', 'Rami Hammad', 'Lynx Hawthorne', 'Calvin Hill', 'Desmine Hilliard', 'Xavien Howard', 'Iain Hunter', 'Jamie Jacobs', 'Tyler Jaynes', 'Johnny Jefferson', 'Chris Johnson', 'Miles Johnson', 'Quan Jones', 'Xavier Jones', 'BJ Jordan', 'Jarrod Koym', 'Jimmy Landes', 'Patrick Lawrence', 'Jay Lee', 'Patrick Levels', 'Ira Lewis', 'Shock Linwood', 'Javonte Magee', 'Blake Mahon', 'Josh Malin', 'Suleiman Masumbuko', 'LaQuan McGowan', 'Kevin Mitchell', 'Kaleb Moore', 'Andrew Morris', 'Blake Muir', 'Sean Muir', 'Silas Nacita', 'Brian Nance', 'Levi Norwood', 'Shawn Oakman', 'Keith Orcutt', 'Jason Osei', 'Jamal Palmer', 'Josh Pelzel', 'Gus Penning', 'Kyle Peterson', 'Bryce Petty', 'Xavier Phillips', 'Chris Platt', 'Alfred Pullom', 'Ryan Reid', 'Tanner Ritchey', 'Andy Ritter', 'Greg Roberts', 'Spencer Roth', 'Seth Russell', 'Chris Sanders', 'Taion Sells', 'Collin Simpson', 'Terrence Singleton', 'KJ Smith', 'Cal Spangler', 'Orion Stewart', 'Tanner Thrift', 'Verkedric Vaughns', 'Chance Waz', 'Anthony Webb', 'Trevor White', 'Terence Williams', 'Ishmael Wilson', 'Tion Wright', 'Taylor Young', 'Ishmael Zamora'],
                    'head_coach': 'Art Briles',
                    'confname': 'Big 12'
                }
        url = urlopen('http://cfdb.me:5000/punt/teams/Baylor')
        data = url.read().decode(url.info().get_param('charset') or 'utf-8')
        d = json.loads(data)
        self.assertEqual(d['location'], team['location'])

    def test_get_teams_6(self):
        team = {
                    'name': 'Texas',
                    'location': 'Austin',
                    'roster': ['Eddie Aboussie', 'Brandon Allen', 'Alex Anderson', 'David Ash', 'Kyle Ashby', 'Andrew Beck', 'Mitchell Becker', 'Roderick Bernard', 'Caleb Bluiett', 'Dillon Boldt', 'John Bonney', 'Cody Boswell', 'Nate Boyer', 'Paul Boyette Jr', 'Malcolm Brown', 'Malcom Brown', 'Donald Catalon', 'Matt Center', 'Demarco Cobbs', 'Adrian Colbert', 'Timothy Cole', 'Bryce Cottrell', 'Dominic Cruciani', 'Terrell Cuney', 'Greg Daniels', 'Michael Davidson', 'Antwuan Davis', 'Deoundrei Davis', 'Gaston Davis', 'Shiro Davis', 'Alex De La Torre', 'Hunter DeGroot', 'Quandre Diggs', 'Taylor Doyle', 'Bryson Echols', 'Steve Edmond', 'Dominic Espinosa', 'Kennedy Estelle', 'Sheroid Evans', 'Sedrick Flowers', 'Poona Ford', 'Armanti Foreman', 'DOnta Foreman', 'Edwin Freeman', 'Dererick Giles', 'Chris Giron', 'Trey Gonzales', 'Garrett Graf', 'Garrett Gray', 'Johnathan Gray', 'Jimmy Greenwood', 'Trenton Hafley', 'Dakota Haines', 'Dylan Haines', 'Jason Hall', 'Cameron Hampton', 'John Harris', 'Desmond Harrison', 'Jerrod Heard', 'Jordan Hicks', 'Jak Holbrook', 'Trey Holtz', 'Devin Huffines', 'Connor Huffman', 'Camrhon Hughes', 'Naashon Hughes', 'Erik Huhn', 'Marcus Hutchins', 'Desmond Jackson', 'Tevin Jackson', 'Darius James', 'Peter Jinkens', 'Lorenzo Joe', 'Daje Johnson', 'Marcus Johnson', 'Nick Jordan', 'Nick Kreider', 'Tyler Lee', 'Dorian Leonard', 'Frank Lopez', 'Tyler Marriott', 'MJ McFarland', 'Jake McMillon', 'Alex Mercado', 'Logan Mills', 'Chris Nelson', 'Alex Norman', 'Jake Oliver', 'Miles Onyegbule', 'Clark Orren', 'Kent Perkins', 'Ben Pruitt', 'Jake Raulerson', 'Cedric Reed', 'Hassan Ridgeway', 'Curtis Riser', 'Derick Roberson', 'Ryan Roberts', 'Jermaine Roberts Jr', 'Daniel Rodriguez', 'Elijah Rodriguez', 'Nick Rose', 'William Russ', 'Dalton Santos', 'Jaxon Shipley', 'Matthew Sims', 'Jordan Strickland', 'Geoff Swaim', 'Tyrone Swoopes', 'Ty Templin', 'Chris Terry', 'David Thomann', 'Duke Thomas', 'Mykkele Thompson', 'Johnny Tseng', 'Josh Turner', 'Kevin Vaccaro', 'Logan Vinklarek', 'Jacorey Warrick', 'Michael Welsh', 'Blake Whiteley', 'Michael Wilson'],
                    'head_coach': 'Charlie Strong',
                    'confname': 'Big 12'
                }
        url = urlopen('http://cfdb.me:5000/punt/teams/Texas')
        data = url.read().decode(url.info().get_param('charset') or 'utf-8')
        d = json.loads(data)
        self.assertEqual(d['location'], team['location'])

    def test_get_teams_7(self):
        team = {
                    'name': 'Texas',
                    'location': 'Austin',
                    'roster': ['Eddie Aboussie', 'Brandon Allen', 'Alex Anderson', 'David Ash', 'Kyle Ashby', 'Andrew Beck', 'Mitchell Becker', 'Roderick Bernard', 'Caleb Bluiett', 'Dillon Boldt', 'John Bonney', 'Cody Boswell', 'Nate Boyer', 'Paul Boyette Jr', 'Malcolm Brown', 'Malcom Brown', 'Donald Catalon', 'Matt Center', 'Demarco Cobbs', 'Adrian Colbert', 'Timothy Cole', 'Bryce Cottrell', 'Dominic Cruciani', 'Terrell Cuney', 'Greg Daniels', 'Michael Davidson', 'Antwuan Davis', 'Deoundrei Davis', 'Gaston Davis', 'Shiro Davis', 'Alex De La Torre', 'Hunter DeGroot', 'Quandre Diggs', 'Taylor Doyle', 'Bryson Echols', 'Steve Edmond', 'Dominic Espinosa', 'Kennedy Estelle', 'Sheroid Evans', 'Sedrick Flowers', 'Poona Ford', 'Armanti Foreman', 'DOnta Foreman', 'Edwin Freeman', 'Dererick Giles', 'Chris Giron', 'Trey Gonzales', 'Garrett Graf', 'Garrett Gray', 'Johnathan Gray', 'Jimmy Greenwood', 'Trenton Hafley', 'Dakota Haines', 'Dylan Haines', 'Jason Hall', 'Cameron Hampton', 'John Harris', 'Desmond Harrison', 'Jerrod Heard', 'Jordan Hicks', 'Jak Holbrook', 'Trey Holtz', 'Devin Huffines', 'Connor Huffman', 'Camrhon Hughes', 'Naashon Hughes', 'Erik Huhn', 'Marcus Hutchins', 'Desmond Jackson', 'Tevin Jackson', 'Darius James', 'Peter Jinkens', 'Lorenzo Joe', 'Daje Johnson', 'Marcus Johnson', 'Nick Jordan', 'Nick Kreider', 'Tyler Lee', 'Dorian Leonard', 'Frank Lopez', 'Tyler Marriott', 'MJ McFarland', 'Jake McMillon', 'Alex Mercado', 'Logan Mills', 'Chris Nelson', 'Alex Norman', 'Jake Oliver', 'Miles Onyegbule', 'Clark Orren', 'Kent Perkins', 'Ben Pruitt', 'Jake Raulerson', 'Cedric Reed', 'Hassan Ridgeway', 'Curtis Riser', 'Derick Roberson', 'Ryan Roberts', 'Jermaine Roberts Jr', 'Daniel Rodriguez', 'Elijah Rodriguez', 'Nick Rose', 'William Russ', 'Dalton Santos', 'Jaxon Shipley', 'Matthew Sims', 'Jordan Strickland', 'Geoff Swaim', 'Tyrone Swoopes', 'Ty Templin', 'Chris Terry', 'David Thomann', 'Duke Thomas', 'Mykkele Thompson', 'Johnny Tseng', 'Josh Turner', 'Kevin Vaccaro', 'Logan Vinklarek', 'Jacorey Warrick', 'Michael Welsh', 'Blake Whiteley', 'Michael Wilson'],
                    'head_coach': 'Charlie Strong',
                    'confname': 'Big 12'
                }
        url = urlopen('http://cfdb.me:5000/punt/teams/Texas')
        data = url.read().decode(url.info().get_param('charset') or 'utf-8')
        d = json.loads(data)
        self.assertEqual(d['head_coach'], team['head_coach'])

    def test_get_teams_8(self):
        team = {
                    'name': 'Baylor',
                    'location': 'Waco',
                    'roster': ['TreVon Armstead', 'Troy Baker', 'Andrew Billings', 'Baylor Black', 'Blake Blackmar', 'Beau Blackshear', 'Jourdan Blake', 'Travon Blanchard', 'Byron Bonds', 'Collin Brence', 'Lee Bristow', 'Terell Brooks', 'Brandon Brown', 'Jarell Broxton', 'Terrell Burt', 'Chris Callahan', 'Grant Campbell', 'KD Cannon', 'Devin Chafin', 'Trevor Clemons-Valdez', 'Pat Colbert', 'Corey Coleman', 'Raaquan Davis', 'Cordell Dorsey', 'Spencer Drango', 'Drew Earnest', 'Cole Edmiston', 'Aiavion Edwards', 'Tyler Edwards', 'Nelson Ehirim', 'Kendall Ehrlich', 'Spencer Evans', 'Jordan Feuerbacher', 'Mallory Franklin', 'Andrew Frerking', 'Clay Fuller', 'Kyle Fuller', 'Antwan Goodley', 'Bryce Hager', 'Davion Hall', 'Rami Hammad', 'Lynx Hawthorne', 'Calvin Hill', 'Desmine Hilliard', 'Xavien Howard', 'Iain Hunter', 'Jamie Jacobs', 'Tyler Jaynes', 'Johnny Jefferson', 'Chris Johnson', 'Miles Johnson', 'Quan Jones', 'Xavier Jones', 'BJ Jordan', 'Jarrod Koym', 'Jimmy Landes', 'Patrick Lawrence', 'Jay Lee', 'Patrick Levels', 'Ira Lewis', 'Shock Linwood', 'Javonte Magee', 'Blake Mahon', 'Josh Malin', 'Suleiman Masumbuko', 'LaQuan McGowan', 'Kevin Mitchell', 'Kaleb Moore', 'Andrew Morris', 'Blake Muir', 'Sean Muir', 'Silas Nacita', 'Brian Nance', 'Levi Norwood', 'Shawn Oakman', 'Keith Orcutt', 'Jason Osei', 'Jamal Palmer', 'Josh Pelzel', 'Gus Penning', 'Kyle Peterson', 'Bryce Petty', 'Xavier Phillips', 'Chris Platt', 'Alfred Pullom', 'Ryan Reid', 'Tanner Ritchey', 'Andy Ritter', 'Greg Roberts', 'Spencer Roth', 'Seth Russell', 'Chris Sanders', 'Taion Sells', 'Collin Simpson', 'Terrence Singleton', 'KJ Smith', 'Cal Spangler', 'Orion Stewart', 'Tanner Thrift', 'Verkedric Vaughns', 'Chance Waz', 'Anthony Webb', 'Trevor White', 'Terence Williams', 'Ishmael Wilson', 'Tion Wright', 'Taylor Young', 'Ishmael Zamora'],
                    'head_coach': 'Art Briles',
                    'confname': 'Big 12'
                }
        url = urlopen('http://cfdb.me:5000/punt/teams/Baylor')
        data = url.read().decode(url.info().get_param('charset') or 'utf-8')
        d = json.loads(data)
        self.assertEqual(d['head_coach'], team['head_coach'])

    def test_get_teams_9(self):
        team = {
                    'name': 'TCU',
                    'location': 'Fort Worth',
                    'roster': ['Zach Allen', 'Garrett Altman', 'Demetrion Amie', 'Jonathan Anderson', 'Philip Armendarez', 'Femi Awe', 'George Baltimore', 'Ty Barrett', 'Luke Benuska', 'Matt Boggs', 'Stacy Boyd', 'Trevone Boykin', 'Chris Bradley', 'Bryson Burtnett', 'Cyd Calvin', 'Justus Canfield', 'Josh Carraway', 'Sam Carter', 'BJ Catalon', 'Chad Childs', 'Colten Christensen', 'LJ Collier', 'Aviante Collins', 'George Cullen', 'Aaron Curry', 'Paul Dawson', 'Ryan DeNucci', 'Josh Doctson', 'Sammy Douglas', 'Michael Downing', 'Keaton Duhon', 'Cameron Echols-Luper', 'Trey Elliott', 'Tayo Fabuluje', 'Brady Foltz', 'Travoskey Garrett', 'Griffin Gilbert', 'Deante Gray', 'Aaron Green', 'Kolby Griffin', 'Ryan Griswold', 'Chris Hackett', 'Travis Hanes', 'Bryson Henderson', 'Blake Henningsen', 'Nathan Hernandez', 'Kyle Hicks', 'Geoff Hooker', 'Travin Howard', 'Joey Hunt', 'Chucky Hunter', 'Kenny Iloka', 'Ridwan Issahaku', 'Matt Joeckel', 'Denzel Johnson', 'Trevorris Johnson', 'Buck Jones', 'Garrett Kaufman', 'Frank Kee', 'Devin Killpatrick', 'Derrick Kindred', 'Bram Kohlhausen', 'Terrell Lathan', 'Tevin Lawson', 'Robert Lewis', 'Kolby Listenbee', 'Michael MacCrory', 'Marcus Mallet', 'Corey McBride', 'Casey McDermott Vai', 'James McFarland', 'Dominic Merka', 'Preston Miller', 'Jordan Moore', 'Patrick Morris', 'Ian Moser', 'Michael Mosharrafa', 'Torrance Mosley', 'Grayson Muehlstein', 'Cliff Murphy', 'Jamelle Naff', 'Shaun Nixon', 'Joseph Noteboom', 'Cole Novak', 'Corry OMeally', 'Jaden Oberkrom', 'Peter Okonofua', 'Nick Orr', 'Connor Osborne', 'Rahmaan Patterson', 'Ethan Perry', 'Keaton Perry', 'Andre Petties-Wilson', 'Davion Pierson', 'David Porter', 'Emanuel Porter', 'James Power', 'Matt Pryor', 'Charlie Reid', 'Foster Sawyer', 'Austin Schlottman', 'Ty Slanina', 'JaJuan Story', 'Ty Summers', 'Phil Taylor', 'Ranthony Texada', 'Bobby Thompson', 'Mike Tuaua', 'Lloyd Tunstill', 'Halapoulivaati Vaitai', 'Daniel Walsh', 'Thomas Walsh', 'Steve Wesley', 'Desmon White', 'Kevin White', 'Paul Whitmill', 'Russell Williams', 'Patrick Zeller'],
                    'head_coach': 'Gary Patterson',
                    'confname': 'Big 12'
                }
        url = urlopen('http://cfdb.me:5000/punt/teams/TCU')
        data = url.read().decode(url.info().get_param('charset') or 'utf-8')
        d = json.loads(data)
        self.assertEqual(d['head_coach'], team['head_coach'])

    def test_get_teams_10(self):
        team = {
                    'name': 'TCU',
                    'location': 'Fort Worth',
                    'roster': ['Zach Allen', 'Garrett Altman', 'Demetrion Amie', 'Jonathan Anderson', 'Philip Armendarez', 'Femi Awe', 'George Baltimore', 'Ty Barrett', 'Luke Benuska', 'Matt Boggs', 'Stacy Boyd', 'Trevone Boykin', 'Chris Bradley', 'Bryson Burtnett', 'Cyd Calvin', 'Justus Canfield', 'Josh Carraway', 'Sam Carter', 'BJ Catalon', 'Chad Childs', 'Colten Christensen', 'LJ Collier', 'Aviante Collins', 'George Cullen', 'Aaron Curry', 'Paul Dawson', 'Ryan DeNucci', 'Josh Doctson', 'Sammy Douglas', 'Michael Downing', 'Keaton Duhon', 'Cameron Echols-Luper', 'Trey Elliott', 'Tayo Fabuluje', 'Brady Foltz', 'Travoskey Garrett', 'Griffin Gilbert', 'Deante Gray', 'Aaron Green', 'Kolby Griffin', 'Ryan Griswold', 'Chris Hackett', 'Travis Hanes', 'Bryson Henderson', 'Blake Henningsen', 'Nathan Hernandez', 'Kyle Hicks', 'Geoff Hooker', 'Travin Howard', 'Joey Hunt', 'Chucky Hunter', 'Kenny Iloka', 'Ridwan Issahaku', 'Matt Joeckel', 'Denzel Johnson', 'Trevorris Johnson', 'Buck Jones', 'Garrett Kaufman', 'Frank Kee', 'Devin Killpatrick', 'Derrick Kindred', 'Bram Kohlhausen', 'Terrell Lathan', 'Tevin Lawson', 'Robert Lewis', 'Kolby Listenbee', 'Michael MacCrory', 'Marcus Mallet', 'Corey McBride', 'Casey McDermott Vai', 'James McFarland', 'Dominic Merka', 'Preston Miller', 'Jordan Moore', 'Patrick Morris', 'Ian Moser', 'Michael Mosharrafa', 'Torrance Mosley', 'Grayson Muehlstein', 'Cliff Murphy', 'Jamelle Naff', 'Shaun Nixon', 'Joseph Noteboom', 'Cole Novak', 'Corry OMeally', 'Jaden Oberkrom', 'Peter Okonofua', 'Nick Orr', 'Connor Osborne', 'Rahmaan Patterson', 'Ethan Perry', 'Keaton Perry', 'Andre Petties-Wilson', 'Davion Pierson', 'David Porter', 'Emanuel Porter', 'James Power', 'Matt Pryor', 'Charlie Reid', 'Foster Sawyer', 'Austin Schlottman', 'Ty Slanina', 'JaJuan Story', 'Ty Summers', 'Phil Taylor', 'Ranthony Texada', 'Bobby Thompson', 'Mike Tuaua', 'Lloyd Tunstill', 'Halapoulivaati Vaitai', 'Daniel Walsh', 'Thomas Walsh', 'Steve Wesley', 'Desmon White', 'Kevin White', 'Paul Whitmill', 'Russell Williams', 'Patrick Zeller'],
                    'head_coach': 'Gary Patterson',
                    'confname': 'Big 12'
                }
        url = urlopen('http://cfdb.me:5000/punt/teams/TCU')
        data = url.read().decode(url.info().get_param('charset') or 'utf-8')
        d = json.loads(data)
        self.assertEqual(d['confname'], team['confname'])

    def test_get_teams_11(self):
        team = {
                    'name': 'Baylor',
                    'location': 'Waco',
                    'roster': ['TreVon Armstead', 'Troy Baker', 'Andrew Billings', 'Baylor Black', 'Blake Blackmar', 'Beau Blackshear', 'Jourdan Blake', 'Travon Blanchard', 'Byron Bonds', 'Collin Brence', 'Lee Bristow', 'Terell Brooks', 'Brandon Brown', 'Jarell Broxton', 'Terrell Burt', 'Chris Callahan', 'Grant Campbell', 'KD Cannon', 'Devin Chafin', 'Trevor Clemons-Valdez', 'Pat Colbert', 'Corey Coleman', 'Raaquan Davis', 'Cordell Dorsey', 'Spencer Drango', 'Drew Earnest', 'Cole Edmiston', 'Aiavion Edwards', 'Tyler Edwards', 'Nelson Ehirim', 'Kendall Ehrlich', 'Spencer Evans', 'Jordan Feuerbacher', 'Mallory Franklin', 'Andrew Frerking', 'Clay Fuller', 'Kyle Fuller', 'Antwan Goodley', 'Bryce Hager', 'Davion Hall', 'Rami Hammad', 'Lynx Hawthorne', 'Calvin Hill', 'Desmine Hilliard', 'Xavien Howard', 'Iain Hunter', 'Jamie Jacobs', 'Tyler Jaynes', 'Johnny Jefferson', 'Chris Johnson', 'Miles Johnson', 'Quan Jones', 'Xavier Jones', 'BJ Jordan', 'Jarrod Koym', 'Jimmy Landes', 'Patrick Lawrence', 'Jay Lee', 'Patrick Levels', 'Ira Lewis', 'Shock Linwood', 'Javonte Magee', 'Blake Mahon', 'Josh Malin', 'Suleiman Masumbuko', 'LaQuan McGowan', 'Kevin Mitchell', 'Kaleb Moore', 'Andrew Morris', 'Blake Muir', 'Sean Muir', 'Silas Nacita', 'Brian Nance', 'Levi Norwood', 'Shawn Oakman', 'Keith Orcutt', 'Jason Osei', 'Jamal Palmer', 'Josh Pelzel', 'Gus Penning', 'Kyle Peterson', 'Bryce Petty', 'Xavier Phillips', 'Chris Platt', 'Alfred Pullom', 'Ryan Reid', 'Tanner Ritchey', 'Andy Ritter', 'Greg Roberts', 'Spencer Roth', 'Seth Russell', 'Chris Sanders', 'Taion Sells', 'Collin Simpson', 'Terrence Singleton', 'KJ Smith', 'Cal Spangler', 'Orion Stewart', 'Tanner Thrift', 'Verkedric Vaughns', 'Chance Waz', 'Anthony Webb', 'Trevor White', 'Terence Williams', 'Ishmael Wilson', 'Tion Wright', 'Taylor Young', 'Ishmael Zamora'],
                    'head_coach': 'Art Briles',
                    'confname': 'Big 12'
                }
        url = urlopen('http://cfdb.me:5000/punt/teams/Baylor')
        data = url.read().decode(url.info().get_param('charset') or 'utf-8')
        d = json.loads(data)
        self.assertEqual(d['confname'], team['confname'])

    def test_get_teams_12(self):
        team = {
                    'name': 'Texas',
                    'location': 'Austin',
                    'roster': ['Eddie Aboussie', 'Brandon Allen', 'Alex Anderson', 'David Ash', 'Kyle Ashby', 'Andrew Beck', 'Mitchell Becker', 'Roderick Bernard', 'Caleb Bluiett', 'Dillon Boldt', 'John Bonney', 'Cody Boswell', 'Nate Boyer', 'Paul Boyette Jr', 'Malcolm Brown', 'Malcom Brown', 'Donald Catalon', 'Matt Center', 'Demarco Cobbs', 'Adrian Colbert', 'Timothy Cole', 'Bryce Cottrell', 'Dominic Cruciani', 'Terrell Cuney', 'Greg Daniels', 'Michael Davidson', 'Antwuan Davis', 'Deoundrei Davis', 'Gaston Davis', 'Shiro Davis', 'Alex De La Torre', 'Hunter DeGroot', 'Quandre Diggs', 'Taylor Doyle', 'Bryson Echols', 'Steve Edmond', 'Dominic Espinosa', 'Kennedy Estelle', 'Sheroid Evans', 'Sedrick Flowers', 'Poona Ford', 'Armanti Foreman', 'DOnta Foreman', 'Edwin Freeman', 'Dererick Giles', 'Chris Giron', 'Trey Gonzales', 'Garrett Graf', 'Garrett Gray', 'Johnathan Gray', 'Jimmy Greenwood', 'Trenton Hafley', 'Dakota Haines', 'Dylan Haines', 'Jason Hall', 'Cameron Hampton', 'John Harris', 'Desmond Harrison', 'Jerrod Heard', 'Jordan Hicks', 'Jak Holbrook', 'Trey Holtz', 'Devin Huffines', 'Connor Huffman', 'Camrhon Hughes', 'Naashon Hughes', 'Erik Huhn', 'Marcus Hutchins', 'Desmond Jackson', 'Tevin Jackson', 'Darius James', 'Peter Jinkens', 'Lorenzo Joe', 'Daje Johnson', 'Marcus Johnson', 'Nick Jordan', 'Nick Kreider', 'Tyler Lee', 'Dorian Leonard', 'Frank Lopez', 'Tyler Marriott', 'MJ McFarland', 'Jake McMillon', 'Alex Mercado', 'Logan Mills', 'Chris Nelson', 'Alex Norman', 'Jake Oliver', 'Miles Onyegbule', 'Clark Orren', 'Kent Perkins', 'Ben Pruitt', 'Jake Raulerson', 'Cedric Reed', 'Hassan Ridgeway', 'Curtis Riser', 'Derick Roberson', 'Ryan Roberts', 'Jermaine Roberts Jr', 'Daniel Rodriguez', 'Elijah Rodriguez', 'Nick Rose', 'William Russ', 'Dalton Santos', 'Jaxon Shipley', 'Matthew Sims', 'Jordan Strickland', 'Geoff Swaim', 'Tyrone Swoopes', 'Ty Templin', 'Chris Terry', 'David Thomann', 'Duke Thomas', 'Mykkele Thompson', 'Johnny Tseng', 'Josh Turner', 'Kevin Vaccaro', 'Logan Vinklarek', 'Jacorey Warrick', 'Michael Welsh', 'Blake Whiteley', 'Michael Wilson'],
                    'head_coach': 'Charlie Strong',
                    'confname': 'Big 12'
                }
        url = urlopen('http://cfdb.me:5000/punt/teams/Texas')
        data = url.read().decode(url.info().get_param('charset') or 'utf-8')
        d = json.loads(data)
        self.assertEqual(d['confname'], team['confname'])

    def test_get_teams_4(self):
        team = {
                    'name': 'TCU',
                    'location': 'Fort Worth',
                    'roster': ['Zach Allen', 'Garrett Altman', 'Demetrion Amie', 'Jonathan Anderson', 'Philip Armendarez', 'Femi Awe', 'George Baltimore', 'Ty Barrett', 'Luke Benuska', 'Matt Boggs', 'Stacy Boyd', 'Trevone Boykin', 'Chris Bradley', 'Bryson Burtnett', 'Cyd Calvin', 'Justus Canfield', 'Josh Carraway', 'Sam Carter', 'BJ Catalon', 'Chad Childs', 'Colten Christensen', 'LJ Collier', 'Aviante Collins', 'George Cullen', 'Aaron Curry', 'Paul Dawson', 'Ryan DeNucci', 'Josh Doctson', 'Sammy Douglas', 'Michael Downing', 'Keaton Duhon', 'Cameron Echols-Luper', 'Trey Elliott', 'Tayo Fabuluje', 'Brady Foltz', 'Travoskey Garrett', 'Griffin Gilbert', 'Deante Gray', 'Aaron Green', 'Kolby Griffin', 'Ryan Griswold', 'Chris Hackett', 'Travis Hanes', 'Bryson Henderson', 'Blake Henningsen', 'Nathan Hernandez', 'Kyle Hicks', 'Geoff Hooker', 'Travin Howard', 'Joey Hunt', 'Chucky Hunter', 'Kenny Iloka', 'Ridwan Issahaku', 'Matt Joeckel', 'Denzel Johnson', 'Trevorris Johnson', 'Buck Jones', 'Garrett Kaufman', 'Frank Kee', 'Devin Killpatrick', 'Derrick Kindred', 'Bram Kohlhausen', 'Terrell Lathan', 'Tevin Lawson', 'Robert Lewis', 'Kolby Listenbee', 'Michael MacCrory', 'Marcus Mallet', 'Corey McBride', 'Casey McDermott Vai', 'James McFarland', 'Dominic Merka', 'Preston Miller', 'Jordan Moore', 'Patrick Morris', 'Ian Moser', 'Michael Mosharrafa', 'Torrance Mosley', 'Grayson Muehlstein', 'Cliff Murphy', 'Jamelle Naff', 'Shaun Nixon', 'Joseph Noteboom', 'Cole Novak', 'Corry OMeally', 'Jaden Oberkrom', 'Peter Okonofua', 'Nick Orr', 'Connor Osborne', 'Rahmaan Patterson', 'Ethan Perry', 'Keaton Perry', 'Andre Petties-Wilson', 'Davion Pierson', 'David Porter', 'Emanuel Porter', 'James Power', 'Matt Pryor', 'Charlie Reid', 'Foster Sawyer', 'Austin Schlottman', 'Ty Slanina', 'JaJuan Story', 'Ty Summers', 'Phil Taylor', 'Ranthony Texada', 'Bobby Thompson', 'Mike Tuaua', 'Lloyd Tunstill', 'Halapoulivaati Vaitai', 'Daniel Walsh', 'Thomas Walsh', 'Steve Wesley', 'Desmon White', 'Kevin White', 'Paul Whitmill', 'Russell Williams', 'Patrick Zeller'],
                    'head_coach': 'Gary Patterson',
                    'confname': 'Big 12'
                }
        url = urlopen('http://cfdb.me:5000/punt/teams/TCU')
        data = url.read().decode(url.info().get_param('charset') or 'utf-8')
        d = json.loads(data)
        self.assertEqual(d['location'], team['location'])

    # -----------
    # get_conf
    # -----------

    def test_get_conf_1(self):
        conf = {
                    'name': 'Big Ten',
                    'founded': '1896',
                    'comm': 'James Delany (since 1989)',
                    'champ': 'Ohio State',
                    'num_teams': '14',
                    'teams': ['Illinois','Indiana', 'Iowa', 'Maryland','Michigan', 'Michigan State', 'Minnesota', 'Nebraska', 'Northwestern', 'Ohio State', 'Penn State', 'Purdue', 'Rutgers', 'Wisconsin']
                }
        url = urlopen('http://cfdb.me:5000/punt/conf/Big%20Ten')
        data = url.read().decode(url.info().get_param('charset') or 'utf-8')
        d = json.loads(data)
        self.assertEqual(d['name'], conf['name'])

    def test_get_conf_2(self):
        conf = {
                    'name': 'Big 12',
                    'founded': '1996',
                    'comm': 'Bob Bowlsby (since 2012)',
                    'champ': 'Baylor',
                    'num_teams': '10',
                    'teams': ['Baylor', 'Iowa State', 'Kansas', 'Kansas State', 'Oklahoma', 'Oklahoma State', 'TCU', 'Texas', 'Texas Tech', 'West Virginia'],
                }
        url = urlopen('http://cfdb.me:5000/punt/conf/Big%2012')
        data = url.read().decode(url.info().get_param('charset') or 'utf-8')
        d = json.loads(data)
        self.assertEqual(d['name'], conf['name'])

    def test_get_conf_3(self):
        conf = {
                    'name': 'SEC',
                    'founded': '1932',
                    'comm': 'Greg Sankey (since 2015)',
                    'champ': 'Alabama',
                    'num_teams': '14',
                    'teams': ['Alabama', 'Arkansas', 'Auburn', 'Florida', 'Georgia', 'Kentucky', 'LSU', 'Mississippi', 'Mississippi State', 'Missouri', 'South Carolina', 'Tennessee', 'Texas A&M', 'Vanderbilt'],
                }
        url = urlopen('http://cfdb.me:5000/punt/conf/SEC')
        data = url.read().decode(url.info().get_param('charset') or 'utf-8')
        d = json.loads(data)
        self.assertEqual(d['name'], conf['name'])

    def test_get_conf_4(self):
        conf = {
                    'name': 'Big Ten',
                    'founded': '1896',
                    'comm': 'James Delany (since 1989)',
                    'champ': 'Ohio State',
                    'num_teams': '14',
                    'teams': ['Illinois','Indiana', 'Iowa', 'Maryland','Michigan', 'Michigan State', 'Minnesota', 'Nebraska', 'Northwestern', 'Ohio State', 'Penn State', 'Purdue', 'Rutgers', 'Wisconsin'],
                }
        url = urlopen('http://cfdb.me:5000/punt/conf/Big%20Ten')
        data = url.read().decode(url.info().get_param('charset') or 'utf-8')
        d = json.loads(data)
        self.assertEqual(d['founded'], conf['founded'])

    def test_get_conf_5(self):
        conf = {
                    'name': 'Big 12',
                    'founded': '1996',
                    'comm': 'Bob Bowlsby (since 2012)',
                    'champ': 'Baylor',
                    'num_teams': '10',
                    'teams': ['Baylor', 'Iowa State', 'Kansas', 'Kansas State', 'Oklahoma', 'Oklahoma State', 'TCU', 'Texas', 'Texas Tech', 'West Virginia'],
                }
        url = urlopen('http://cfdb.me:5000/punt/conf/Big%2012')
        data = url.read().decode(url.info().get_param('charset') or 'utf-8')
        d = json.loads(data)
        self.assertEqual(d['founded'], conf['founded'])

    def test_get_conf_6(self):
        conf = {
                    'name': 'SEC',
                    'founded': '1932',
                    'comm': 'Greg Sankey (since 2015)',
                    'champ': 'Alabama',
                    'num_teams': '14',
                    'teams': ['Alabama', 'Arkansas', 'Auburn', 'Florida', 'Georgia', 'Kentucky', 'LSU', 'Mississippi', 'Mississippi State', 'Missouri', 'South Carolina', 'Tennessee', 'Texas A&M', 'Vanderbilt'],
                }
        url = urlopen('http://cfdb.me:5000/punt/conf/SEC')
        data = url.read().decode(url.info().get_param('charset') or 'utf-8')
        d = json.loads(data)
        self.assertEqual(d['founded'], conf['founded'])

    def test_get_conf_7(self):
        conf = {
                    'name': 'Big Ten',
                    'founded': '1896',
                    'comm': 'James Delany (since 1989)',
                    'champ': 'Ohio State',
                    'num_teams': '14',
                    'teams': ['Illinois','Indiana', 'Iowa', 'Maryland','Michigan', 'Michigan State', 'Minnesota', 'Nebraska', 'Northwestern', 'Ohio State', 'Penn State', 'Purdue', 'Rutgers', 'Wisconsin'],
                }
        url = urlopen('http://cfdb.me:5000/punt/conf/Big%20Ten')
        data = url.read().decode(url.info().get_param('charset') or 'utf-8')
        d = json.loads(data)
        self.assertEqual(d['comm'], conf['comm'])

    def test_get_conf_8(self):
        conf = {
                    'name': 'Big 12',
                    'founded': '1996',
                    'comm': 'Bob Bowlsby (since 2012)',
                    'champ': 'Baylor',
                    'num_teams': '10',
                    'teams': ['Baylor', 'Iowa State', 'Kansas', 'Kansas State', 'Oklahoma', 'Oklahoma State', 'TCU', 'Texas', 'Texas Tech', 'West Virginia'],
                }
        url = urlopen('http://cfdb.me:5000/punt/conf/Big%2012')
        data = url.read().decode(url.info().get_param('charset') or 'utf-8')
        d = json.loads(data)
        self.assertEqual(d['comm'], conf['comm'])

    def test_get_conf_9(self):
        conf = {
                    'name': 'SEC',
                    'founded': '1932',
                    'comm': 'Greg Sankey (since 2015)',
                    'champ': 'Alabama',
                    'num_teams': '14',
                    'teams': ['Alabama', 'Arkansas', 'Auburn', 'Florida', 'Georgia', 'Kentucky', 'LSU', 'Mississippi', 'Mississippi State', 'Missouri', 'South Carolina', 'Tennessee', 'Texas A&M', 'Vanderbilt'],
                }
        url = urlopen('http://cfdb.me:5000/punt/conf/SEC')
        data = url.read().decode(url.info().get_param('charset') or 'utf-8')
        d = json.loads(data)
        self.assertEqual(d['comm'], conf['comm'])

    def test_get_conf_10(self):
        conf = {
                    'name': 'Big Ten',
                    'founded': '1896',
                    'comm': 'James Delany (since 1989)',
                    'champ': 'Ohio State',
                    'num_teams': '14',
                    'teams': ['Illinois','Indiana', 'Iowa', 'Maryland','Michigan', 'Michigan State', 'Minnesota', 'Nebraska', 'Northwestern', 'Ohio State', 'Penn State', 'Purdue', 'Rutgers', 'Wisconsin'],
                }
        url = urlopen('http://cfdb.me:5000/punt/conf/Big%20Ten')
        data = url.read().decode(url.info().get_param('charset') or 'utf-8')
        d = json.loads(data)
        self.assertEqual(d['champ'], conf['champ'])

    def test_get_conf_11(self):
        conf = {
                    'name': 'Big 12',
                    'founded': '1996',
                    'comm': 'Bob Bowlsby (since 2012)',
                    'champ': 'Baylor',
                    'num_teams': '10',
                    'teams': ['Baylor', 'Iowa State', 'Kansas', 'Kansas State', 'Oklahoma', 'Oklahoma State', 'TCU', 'Texas', 'Texas Tech', 'West Virginia'],
                }
        url = urlopen('http://cfdb.me:5000/punt/conf/Big%2012')
        data = url.read().decode(url.info().get_param('charset') or 'utf-8')
        d = json.loads(data)
        self.assertEqual(d['champ'], conf['champ'])

    def test_get_conf_12(self):
        conf = {
                    'name': 'SEC',
                    'founded': '1932',
                    'comm': 'Greg Sankey (since 2015)',
                    'champ': 'Alabama',
                    'num_teams': '14',
                    'teams': ['Alabama', 'Arkansas', 'Auburn', 'Florida', 'Georgia', 'Kentucky', 'LSU', 'Mississippi', 'Mississippi State', 'Missouri', 'South Carolina', 'Tennessee', 'Texas A&M', 'Vanderbilt'],
                }
        url = urlopen('http://cfdb.me:5000/punt/conf/SEC')
        data = url.read().decode(url.info().get_param('charset') or 'utf-8')
        d = json.loads(data)
        self.assertEqual(d['champ'], conf['champ'])

    def test_get_conf_13(self):
        conf = {
                    'name': 'Big Ten',
                    'founded': '1896',
                    'comm': 'James Delany (since 1989)',
                    'champ': 'Ohio State',
                    'num_teams': '14',
                    'teams': ['Illinois','Indiana', 'Iowa', 'Maryland','Michigan', 'Michigan State', 'Minnesota', 'Nebraska', 'Northwestern', 'Ohio State', 'Penn State', 'Purdue', 'Rutgers', 'Wisconsin'],
                }
        url = urlopen('http://cfdb.me:5000/punt/conf/Big%20Ten')
        data = url.read().decode(url.info().get_param('charset') or 'utf-8')
        d = json.loads(data)
        self.assertEqual(d['num_teams'], conf['num_teams'])

    def test_get_conf_14(self):
        conf = {
                    'name': 'Big 12',
                    'founded': '1996',
                    'comm': 'Bob Bowlsby (since 2012)',
                    'champ': 'Baylor',
                    'num_teams': '10',
                    'teams': ['Baylor', 'Iowa State', 'Kansas', 'Kansas State', 'Oklahoma', 'Oklahoma State', 'TCU', 'Texas', 'Texas Tech', 'West Virginia'],
                }
        url = urlopen('http://cfdb.me:5000/punt/conf/Big%2012')
        data = url.read().decode(url.info().get_param('charset') or 'utf-8')
        d = json.loads(data)
        self.assertEqual(d['num_teams'], conf['num_teams'])

    def test_get_conf_15(self):
        conf = {
                    'name': 'SEC',
                    'founded': '1932',
                    'comm': 'Greg Sankey (since 2015)',
                    'champ': 'Alabama',
                    'num_teams': '14',
                    'teams': ['Alabama', 'Arkansas', 'Auburn', 'Florida', 'Georgia', 'Kentucky', 'LSU', 'Mississippi', 'Mississippi State', 'Missouri', 'South Carolina', 'Tennessee', 'Texas A&M', 'Vanderbilt'],
                }
        url = urlopen('http://cfdb.me:5000/punt/conf/SEC')
        data = url.read().decode(url.info().get_param('charset') or 'utf-8')
        d = json.loads(data)
        self.assertEqual(d['num_teams'], conf['num_teams'])

# ----
# main
# ----

if __name__ == "__main__":
    main()

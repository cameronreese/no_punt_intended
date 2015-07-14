#!/usr/bin/env python3

# Modified some code from StackOverflow.com

from urllib.request import urlopen
from bs4 import BeautifulSoup

d = {140: 'Cincinnati', 164: 'Connecticut', 196: 'East Carolina', 288: 'Houston', 404: 'Memphis', 651: 'South Florida', 663: 'SMU', 690: 'Temple', 718: 'Tulane', 719: 'Tulsa', 128: 'UCF', 67: 'Boston College', 147: 'Clemson', 193: 'Duke', 234: 'Florida State', 255: 'Georgia Tech', 367: 'Louisville', 415: "Miami", 457: 'North Carolina', 490: 'North Carolina State', 545: 'Pittsburgh', 688: 'Syracuse', 746: 'Virginia', 742: 'Virginia Tech', 749: 'Wake Forest', 51: 'Baylor', 311: 'Iowa State', 328: 'Kansas State', 522: 'Oklahoma', 521: 'Oklahoma State', 698: 'TCU', 703: 'Texas', 700: 'Texas Tech', 768: 'West Virginia', 301: 'Illinois', 306: 'Indiana', 312: 'Iowa', 392: 'Maryland', 418: 'Michigan', 416: 'Michigan State', 428: 'Minnesota', 463: 'Nebraska', 509: 'Northwestern', 518: 'Ohio State', 539: 'Penn State', 559: 'Purdue', 587: 'Rutgers', 796: 'Wisconsin', 229: 'Florida Atlantic', 231: 'Florida International', 366: 'Louisiana Tech', 388: 'Marshall', 419: 'Middle Tennessee', 497: 'North Texas', 523: 'Old Dominion', 574: 'Rice', 664: 'Southern Mississippi', 9: 'UAB', 704: 'UTEP', 706: 'UTSA', 772: 'Western Kentucky', 725: 'Army', 77: 'BYU', 726: 'Navy', 513: 'Notre Dame', 5: 'Akron', 47: 'Ball State', 71: 'Bowling Green', 86: 'Buffalo', 129: 'Central Michigan', 204: 'Eastern Michigan', 331: 'Kent State', 400: 'Massachusetts', 414: 'Miami (Ohio)', 503: 'Northern Illinois', 519: 'Ohio', 709: 'Toledo', 774: 'Western Michigan', 721: 'Air Force', 66: 'Boise State', 156: 'Colorado State', 96: 'Fresno State', 277: 'Hawaii', 466: 'Nevada', 473: 'New Mexico', 626: 'San Diego State', 630: 'San Jose State', 465: 'UNLV', 731: 'Utah State', 811: 'Wyoming', 29: 'Arizona', 28: 'Arizona State', 107: 'California', 157: 'Colorado', 529: 'Oregon', 528: 'Oregon State', 657: 'USC', 674: 'Stanford', 110: 'UCLA', 732: 'Utah', 756: 'Washington', 754: 'Washington State', 8: 'Alabama', 31: 'Arkansas', 37: 'Auburn', 235: 'Florida', 257: 'Georgia', 334: 'Kentucky', 365: 'LSU', 433: 'Mississippi', 430: 'Mississippi State', 434: 'Missouri', 648: 'South Carolina', 694: 'Tennessee', 697: 'Texas A&M', 736: 'Vanderbilt', 27: 'Appalachian State', 30: 'Arkansas State', 253: 'Georgia Southern', 254: 'Georgia State', 295: 'Idaho', 671: 'Louisiana-Lafayette', 498: 'Louisiana-Monroe', 472: 'New Mexico State', 646: 'South Alabama', 670: 'Texas State', 716: 'Troy'}

for key, values in d.items() :
	data = urlopen('http://www.cfbstats.com/2014/team/' + str(key) + '/roster.html')
	soup = BeautifulSoup(data.read()) 

	# print(values)
	for row in soup('tr')[1:]:
	    data = [str(i.getText()) for i in row('td')]
	    data = [str(values)] + data
	    # link = row('td')[1]('a') 
	    # if len(link) > 0:
	    #     link = str(link[0]['href'])
	    #     data = [str(link)] + data
	    print(data)
	    print('\n')
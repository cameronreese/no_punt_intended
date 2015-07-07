#!/usr/bin/env python3

from urllib.request import urlopen
from bs4 import BeautifulSoup

d = {140: 'Cincinnati', 164: 'Connecticut', 196: 'East Carolina', 288: 'Houston', 404: 'Memphis', 651: 'South Florida', 663: 'Southern Mississippi', 690: 'Temple', 718: 'Tulane', 719: 'Tulsa', 128: 'Central Florida', 67: 'Boston College', 147: 'Clemson', 193: 'Duke', 234: 'Florida State', 255: 'Georgia Tech', 367: 'Louisville', 415: "Miami FL", 457: 'North Carolina', 490: 'North Carolina State', 545: 'Pittsburgh', 688: 'Syracuse', 746: 'Virginia', 742: 'Virginia Tech', 749: 'Wake Forest', 51: 'Baylor', 311: 'Iowa State', 328: 'Kansas State', 522: 'Oklahoma', 521: 'Oklahoma State', 698: 'Texas Christian', 703: 'Texas', 700: 'Texas Tech', 768: 'West Virginia', 301: 'Illinois', 306: 'Indiana', 312: 'Iowa', 392: 'Maryland', 418: 'Michigan', 416: 'Michigan State', 428: 'Minnesota', 463: 'Nebraska', 509: 'Northwestern', 518: 'Ohio State', 539: 'Penn State', 559: 'Purdue', 587: 'Rutgers', 796: 'Wisconsin', 229: 'Florida Atlantic', 231: 'Florida International', 366: 'Louisiana Tech', 388: 'Marshall', 419: 'Middle Tennessee State', 497: 'North Texas', 523: 'Old Dominion', 574: 'Rice', 664: 'Southern Mississippi', 9: 'Alabama-Birmingham', 704: 'Texas El Paso', 706: 'Texas San Antonio', 772: 'Western Kentucky', 725: 'Army', 77: 'Brigham-Young', 726: 'Navy', 513: 'Notre Dame', 5: 'Akron', 47: 'Ball State', 71: 'Bowling Green', 86: 'Buffalo', 129: 'Central Michigan', 204: 'Eastern Michigan', 331: 'Kent State', 400: 'Massachusetts', 414: 'Miami OH', 503: 'Northern Illinois', 519: 'Ohio', 709: 'Toledo', 774: 'Western Michigan', 721: 'Air Force', 66: 'Boise State', 156: 'Colorado State', 96: 'Fresno State', 277: 'Hawaii', 466: 'Nevada', 473: 'New Mexico', 626: 'San Diego State', 630: 'San Jose State', 465: 'Nevada Las Vegas', 731: 'Utah State', 811: 'Wyoming', 29: 'Arizona', 28: 'Arizona State', 107: 'California', 157: 'Colorado', 529: 'Oregon', 528: 'Oregon State', 657: 'South Carolina', 674: 'Stanford', 110: 'UCLA', 732: 'Utah', 756: 'Washington', 754: 'Washington State', 8: 'Alabama', 31: 'Arkansas', 37: 'Auburn', 235: 'Florida', 257: 'Georgia', 334: 'Kentucky', 365: 'Louisiana State', 433: 'Mississippi', 430: 'Mississippi State', 434: 'Missouri', 648: 'South Carolina', 694: 'Tennessee', 697: 'Texas A&M', 736: 'Vanderbilt', 27: 'Appalachian State', 30: 'Arkansas State', 253: 'Georgia Southern', 254: 'Georgia State', 295: 'Idaho', 671: 'Louisiana-Lafayette', 498: 'Louisiana-Monroe', 472: 'New Mexico State', 646: 'South Alabama', 670: 'Texas State', 716: 'Troy State'}

for key, value in d.items() :
	# newStr = ""
	letter = "" 
	# string = value
	letter = value[0].lower()
	value = value.replace(' ', '_').replace('-', '_').lower()
	# newStr = newStr.replace('-', '_')

	data = urlopen('http://www.cfbdatawarehouse.com/data/active/' + str(letter)  + '/' + str(value) + '/index.php')
	soup = BeautifulSoup(data.read()) # creates a BS4 HTML parsing object


	print('Colleges: ' + value + '\n')
	# data = [str(i.getText()) for i in soup('p style')[1:]]
		# data = [str(i.getText()) for i in row('td')]
	
	#print(value)
	# for row in soup('p'):
	# data = [str(i.getText()) for i in row('b')]
	stats = soup.findAll("p", style = "margin-left: 15; margin-top: 5; margin-bottom: 5")
	for text in stats:
		print(text.find('b').string)
		print('\n')
	# stats.contents
	# b1 = "<b>"
	# b2 = "</b>"
	# text = ""
	# for i in stats:
	# 	if i[stats] == 'b' and i[stats + 1] == '>':
	# 		while i[stats] != '<':
	# 			text += i[stats]

	# print(stats.contents)
	# print('\n')
	#     #link = row('td')[1]('a') # the linked player
	#     if len(link) > 0:
	#         link = str(link[0]['href'])
	#         data = [str(link)] + data
	#     print(data)
	#     print('\n')
#!/usr/bin/env python3

import urllib, re
import fileinput


d = {}

for line in fileinput.input():

	source = urllib.urlopen(line).read()

	for j in re.findall('/collegefootball/players/playerpage/[0-9]*/[a-z-]*', source):
		
		source2 = urllib.urlopen('http://www.cbssports.com' + str(j)).read()

		for link in re.findall('http://sports.cbsimg.net/images/collegefootball/players/60x80/[0-9]*.jpg', source2):
			site = j.rsplit('/',1)
			site = site[1]
			site = site.replace('-', ' ')
			d[str(site)] = link

print d
	
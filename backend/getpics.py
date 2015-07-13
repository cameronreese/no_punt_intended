#!/usr/bin/env python3

# Modified some code from StackOverflow.com

# import urllib, re
# from urllib.request import urlopen
# from bs4 import BeautifulSoup

# d = {}
 
# ## every image name is an abbreviation composed by capital letters, so...
# for i in range(3000000):
# 	key = ('http://www.cbssports.com/collegefootball/players/playerpage/' + str(i))
# # for k, n in urlopen('http://www.cbssports.com/collegefootball/players/playerpage/' + k + '/' + n):
#     #print link
# 	# data = urlopen('http://www.cbssports.com/collegefootball/players/playerpage/' + k + '/' + n)
# 	# soup = BeautifulSoup(key.read())
# 	print(key)

import urllib, re
import fileinput


d = {}

# source = urllib.urlopen('http://www.cbssports.com/collegefootball/players').read()

# for i in re.findall('/collegefootball/teams/roster/[A-Z]*/[a-z-]*', source):
# 	print 'http://www.cbssports.com' + str(i)

for line in fileinput.input():
	# process(line)

	source = urllib.urlopen(line).read()


	# source2 = urllib.urlopen('http://www.cbssports.com' + str(i)).read()
	# # print source2

	for j in re.findall('/collegefootball/players/playerpage/[0-9]*/[a-z-]*', source):
		
		source2 = urllib.urlopen('http://www.cbssports.com' + str(j)).read()
		

		# print source3

		for link in re.findall('http://sports.cbsimg.net/images/collegefootball/players/60x80/[0-9]*.jpg', source2):
			site = j.rsplit('/',1)
			site = site[1]
			site = site.replace('-', ' ')
			d[str(site)] = link

print d
	

## every image name is an abbreviation composed by capital letters, so...
	# for pic in re.findall('http://sports.cbsimg.net/images/collegefootball/players/60x80/[0-9]*.jpg', link):
	#     print pic


	    ## the code above just prints the link;
	    ## if you want to actually download, set the flag below to True

	    # actually_download = False
	    # if actually_download:
	    #     filename = link.split('/')[-1]
	    #     urllib.urlretrieve(link, filename)

	# key = k
	# value = name

# print(d)
    

    ## the code above just prints the link;
    ## if you want to actually download, set the flag below to True

    # actually_download = True
    # if actually_download:
    #     filename = link.split('/')[-1]
    #     urllib.urlretrieve(link, filename)

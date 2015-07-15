#!/usr/bin/env python3

from urllib2 import Request, urlopen, URLError

request = request('http://placekitten.com')

try:
	response = urlopen(request)
	kittens = response.read()
	print kittens[559:1000]
except URLError, e:
	print 'No kittez. Got error code:', e

	kittens = urlopen('http://placekitten.com/200/300')
	f = open('kittens.jpg', 'wb')
	f.write(kittens.read())
	f.close()
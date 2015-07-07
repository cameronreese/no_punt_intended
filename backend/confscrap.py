#!/usr/bin/env python3

from urllib.request import urlopen
from bs4 import BeautifulSoup

data = urlopen('https://en.wikipedia.org/wiki/List_of_NCAA_conferences')
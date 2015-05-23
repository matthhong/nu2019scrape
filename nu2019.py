from collections import defaultdict as ddict
import csv
import mechanize
from bs4 import BeautifulSoup as bs

def searchName(firstName, lastName):
	br = mechanize.Browser()
	br.set_handle_robots(False)

	br.open('http://directory.northwestern.edu/?a=1')

	br.select_form('phadv')
	br.form['name'] = 'Matt Hong'
	br.form['affiliations'] = ['student']

	br.submit()

	response = br.response()

	print response.read()

def getNameDict(filename):
	nameDict = ddict(list)

	with open(filename) as infile:
		reader = csv.reader(infile, delimiter = ',')
		for row in reader:
			name = row[0]
			for nickname in row[1:]:
				nameDict[nickname].append(name)

	return nameDict


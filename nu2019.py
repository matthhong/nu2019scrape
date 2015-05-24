from collections import defaultdict as ddict
import csv
import mechanize
import pythonParser as parser
from bs4 import BeautifulSoup as Soup

br = mechanize.Browser()
br.set_handle_robots(False)

br.open('http://directory.northwestern.edu/?a=1')

def searchName(firstName, lastName):
	br.select_form('phadv')
	br.form['first_name'] = firstName
	br.form['last_name'] = lastName
	br.form['affiliations'] = ['student']
	br.submit()

	response = br.response().read()
	soup = Soup(response)

	links = soup.body.find(id='content').findAll('a')

	emails = []
	for link in links:
		target = link.get('href')
		if 'mailto' in target:
			emails.append(target[7:])

	return emails

def getNameDict(csvFile, txtFile):
	nameDict = ddict(list)

	with open(csvFile) as infile:
		reader = csv.reader(infile, delimiter = ',')
		for row in reader:
			name = row[0]
			for nickname in row[1:]:
				nameDict[nickname].append(name)

	with open(txtFile) as infile:
		reader = csv.reader(infile, delimiter ='\t')
		for row in reader:
			nickname = row[0].lower()
			name = row[1].lower()
			if name not in nameDict[nickname]:
				nameDict[nickname].append(name)

	return nameDict

def get2019Names(txtfile):
	possibleNames = []
	nameDict = getNameDict('names.csv', 'nicknames.txt')

	with open(txtfile) as infile:
		reader = csv.reader(infile, delimiter = ' ')
		reader.next()

		for row in reader:
			firstName = row[0].lower()
			lastName = row[-1].lower()
			possibleNames.append((firstName, lastName))

			possibleFirstNames = nameDict[firstName]
			for name in possibleFirstNames:
				possibleNames.append((name, lastName))

	return possibleNames




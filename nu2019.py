import mechanize
from bs4 import BeautifulSoup as bs

br = mechanize.Browser()
br.set_handle_robots(False)

br.open('http://directory.northwestern.edu/?a=1')

br.select_form('phadv')
br.form['name'] = 'Matt Hong'
br.form['affiliations'] = ['student']

br.submit()

response = br.response()

print response.read()
import mechanize

br = mechanize.Browser()
br.set_handle_robots(False)

br.open('http://directory.northwestern.edu/?a=1')

response = br.response()

print response.geturl()
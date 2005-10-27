# -*- coding: utf-8 -*-
"""
morfix translator

@copyright: Copyright 2004 by omri <omri.il@gmail.com>
@license: GNU GPL, see COPYING for details
"""

import re
import httplib
import urllib


# Map morfix keys to human readable keys
morfixToHuman = {'H': 'word', 'HD': 'type', 'E': 'translation'}

parse_re = re.compile(r'''
^document\.all\[\'Option                    # start
(?P<key>H|HD|E)(?P<index>\d)                # key
\'\]\.innerText\s*=\s*"(?P<value>.+)"\s*$   # value
''', re.VERBOSE | re.MULTILINE | re.UNICODE)

choice_re = re.compile(r'if \(choice == (?P<id>[0-9]+)\)\{(?P<code>[^\}]+)\}')

solutions_re = re.compile(r'<INPUT TYPE=\"RADIO\" NAME= \"salutation\" (?:checked  )?Value= \"(?P<value>[^\"]+)\"  onClick="PrintWordTrans\((?P<id>[0-9]+)\)">')


def parse(html):
	"""
	Parse html string, return dict of translations 
	
	@param html: html from morfix (unicode)
	@rtype: list of dicts
	@return: list of translations
	"""
	solutions = {}
	for i in solutions_re.finditer(html):
		groupdict = i.groupdict()
		solutions[int(groupdict['id'])] = groupdict['value']
	#print solutions
	ret = []
	
	for i in choice_re.finditer(html):
		word = i.groupdict()
		translations = {}
		for match in parse_re.finditer(word['code']):
			d = match.groupdict()
			value = d['value'].strip()
			if value:
				index = int(d['index'])
				if not translations.has_key(index):
					translations[index] = {}
					for dictvalue in morfixToHuman.values():
						translations[index][dictvalue] = '-'
				key = morfixToHuman[d['key']]
				translations[index][key] = value
		# Make a list of translations
		#keys = translations.keys()
		#keys.sort()
		ret.append((solutions[int(word['id'])], translations.values()))
	return ret


def translate(word):
	"""
	Send a query to morfix and parse the html 
	
	@param word: word to translate (unicode)
	@rtype: list of dicts
	@return: list of translations
	"""
	params = urllib.urlencode({'q': word.encode('cp1255')})
	headers = {"Content-type": "application/x-www-form-urlencoded"}
	
	# For getting the translation we need to have ASPSESSIONID.
	conn = httplib.HTTPConnection("milon.morfix.co.il")
	conn.request("POST", "/default.asp", params, headers)
	response = conn.getresponse()
	headers['Cookie'] = response.getheader('Set-Cookie')
	conn.close()
	
	# Get the translation
	conn.request("GET", "/default2.asp", params, headers)
	response = conn.getresponse()
	data = response.read().decode('cp1255', 'ignore')
	conn.close()
	
	# Parse the data and fill a list with the results
	return parse(data)
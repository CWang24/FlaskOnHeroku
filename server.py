#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import os
import requests
import re
from flask import render_template
from flask import Flask, request, url_for

app = Flask(__name__)
app.secret_key = 'This is really unique and secret'

# @app.route('/')
# def hello_person():
	# return """
		# <p>Who do you want me to say "Hi" toasdfasdfasdf?</p>
		# <form method="POST" action="%s"><input name="person" /><input type="submit" value="Go!" /></form>
		# """ % (url_for('greet'),)

# @app.route('/greet1', methods=['POST'])
# def greet():
	# greeting = random.choice(["Hiya", "Hallo", "Hola", "Ola", "Salut", "Privet", "Konnichiwa", "Ni hao"])
	# return """
		# <p>%s, %s!</p>
		# <p><a href="%s">Back to start</a></p>
		# <p><a href="%s">test</a></p>
		# """ % (greeting, request.form["person"], url_for('hello_person'), url_for('test'))
		
		
@app.route('/')
def RTFCP():
	address = {}
	GKpopul={} 
	GKpopul_numbers={} 
	address['APink'] = 'http://cafe.daum.net/_c21_/home?grpid=1Mg8v'
	address['IU'] = 'http://cafe.daum.net/_c21_/home?grpid=1I7Yc'
	address['girlsday'] = 'http://cafe.daum.net/_c21_/home?grpid=1Maq7'
	address['4minute'] = 'http://cafe.daum.net/_c21_/home?grpid=1Hmfs'
	address['T-ara'] = 'http://cafe.daum.net/_c21_/home?grpid=1Pux2'
	address['SPICA'] = 'http://cafe.daum.net/_c21_/home?grpid=1PNXb'
	address['SISTAR'] = 'http://cafe.daum.net/_c21_/home?grpid=1LTUi'
	address['AOA'] = 'http://cafe.daum.net/_c21_/home?grpid=1QOHC'
	address['Hello Venus'] = 'http://cafe.daum.net/_c21_/home?grpid=1PxoY'
	address['Wonder Girls'] = 'http://cafe.daum.net/_c21_/home?grpid=19KPA'
	address['2ne1(Dcafe)'] = 'http://cafe.daum.net/_c21_/home?grpid=1HN86'
	# address['2ne1_Ncafe'] = 'http://'
	address['f(x)'] = 'http://cafe.daum.net/_c21_/home?grpid=SZ5S'
	address['BEG'] = 'http://cafe.daum.net/_c21_/home?grpid=15Lhi'
	address['Kara'] = 'http://cafe.daum.net/_c21_/home?grpid=u0v3'
	address['Miss A'] = 'http://cafe.daum.net/_c21_/home?grpid=1L9ty'
	address['Lovelyz'] = 'http://cafe.daum.net/_c21_/home?grpid=1PKNB'
	address['Secret'] = 'http://cafe.daum.net/_c21_/home?grpid=1IvqZ'
	address['MAMAMOO'] = 'http://cafe.daum.net/_c21_/home?grpid=1Tj9f'
	address['EXID'] = 'http://cafe.daum.net/_c21_/home?grpid=1OyFk'
	address['Davichi'] = 'http://cafe.daum.net/_c21_/home?grpid=1CXAK'
	address['9Muses'] = 'http://cafe.daum.net/_c21_/home?grpid=1L7pi'
	address['Afterschool'] = 'http://cafe.daum.net/_c21_/home?grpid=1Gnqy'
	address['Red Velvet'] = 'http://cafe.daum.net/_c21_/home?grpid=1UV3J'
	address['Crayon Pop'] = 'http://cafe.daum.net/_c21_/home?grpid=1RjxX'
	address['Gfriend'] = 'http://cafe.daum.net/_c21_/home?grpid=1Ugs2'
	address['Ladies Code'] = 'http://cafe.daum.net/_c21_/home?grpid=1Rdps'
	address['OH MY GIRL'] = 'http://cafe.daum.net/_c21_/home?grpid=1VTSi'
	address['Juniel'] = 'http://cafe.daum.net/_c21_/home?grpid=1O9vs'
	address['Gavy NJ'] = 'http://cafe.daum.net/_c21_/home?grpid=11eyP'
	address['BESTie'] = 'http://cafe.daum.net/_c21_/home?grpid=1SHLU'
	address['Rainbow'] = 'http://cafe.daum.net/_c21_/home?grpid=1QZ2z'
	address['CLC'] = 'http://cafe.daum.net/_c21_/home?grpid=1Uj85'
	address['Sunny Hill'] = 'http://cafe.daum.net/_c21_/home?grpid=1NkMz'
	address['FIESTAR'] = 'http://cafe.daum.net/_c21_/home?grpid=1QZED'
	address['SONAMOO'] = 'http://cafe.daum.net/_c21_/home?grpid=1UnxS'
	address['Stellar'] = 'http://cafe.daum.net/_c21_/home?grpid=1OFNR'
	address['N.CA(Ncafe)'] = 'http://cafe.naver.com/lovenca'
	address['RANIA'] = 'http://cafe.daum.net/_c21_/home?grpid=1FSh4'
	# address[''] = 'http://'
	# address[''] = 'http://'
	# address[''] = 'http://'
	address['April'] = 'http://cafe.daum.net/_c21_/home?grpid=1W0a2'
	address['SNSD(Dcafe)'] = 'http://cafe.daum.net/_c21_/home?grpid=8S3R'
	address['SNSD(Ncafe)'] = 'http://cafe.naver.com/tmfql8967'
	
	for girlgroup in address:
		url=address[girlgroup]
		r = requests.get(url)
		result = r.text
		pattern1= re.compile("memberlist.+>(.+)</a></span></li>") #daum cafe
		m1=re.search(pattern1,result)
		if m1:
			GKpopul[girlgroup]=m1.group(1)
			GKpopul_numbers[girlgroup]=int(m1.group(1).replace(',', ''))
	
	ranklist = sorted(GKpopul_numbers.values(),reverse = True)
	ranktable=[]
	rank=1
	for ppl in ranklist:
		for gg in GKpopul_numbers:
			if GKpopul_numbers[gg] == ppl and rank<36:
				ranktable.append({'ggname':gg, 'ggppl':GKpopul[gg], 'ggrank':rank})
				rank=rank+1

	
	return render_template("index.html",
        title = 'Offical Cafe Real Time Population',
        list = ranktable)

	
if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)

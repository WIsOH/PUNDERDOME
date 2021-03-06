from flask import Flask, render_template, request, send_from_directory
import json, random, os, re

app = Flask(__name__)

with open('static/phrases.txt') as f:
    phrases = f.readlines()

ignore = ['i', 'a', 'an', 'the']

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'GET':				
		return render_template('index.html')
	elif request.method == 'POST':
		return render_template('index.html', genpun=random.choice(phrases))

@app.route('/egg')
def egg():
	return render_template('egg.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/aboutegg')
def aboutegg():
	return render_template('aboutegg.html')

if __name__ == "__main__":
	app.debug = True
	app.run()


from flask import Flask, render_template, request
import json, random

app = Flask(__name__)

f = open('static/phrases.txt')
lines = f.read().split('\n')
f.close()

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		return render_template('index.html')
	elif request.method == 'POST':
		lines = [1, 2, 3, 4]
#		f = open('static/phrases.txt')
#		lines = f.read().split('\n')
#		f.close()
		#phrases = [phrases.rstrip('\n') for line in open('static/phrases.txt')]
		return render_template('index.html', genpun=random.choice(lines))

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


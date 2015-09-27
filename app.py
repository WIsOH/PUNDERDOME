from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
	if request.method == 'POST'

@app.route('/about')
def about():
	return render_template('about.html')

# debugging
@app.route('/hello')
def hello():
	return render_template('hello.html')
	

if __name__ == "__main__":
	app.debug = True
	app.run()


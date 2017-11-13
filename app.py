from flask import Flask, render_template, jsonify
import random, logging
import os

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler())
app.logger.setLevel(logging.INFO)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/status.json')
def status():
	name = ''
	try:
		name = os.environ['MY_POD_NAME']
	except Exception as e: 
		name = 'no-names'
		print e
	return jsonify({'name':name})

if __name__ == "__main__":
    app.run(host="0.0.0.0")

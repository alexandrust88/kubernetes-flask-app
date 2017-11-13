from flask import Flask, render_template
import random, logging
import os

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler())
app.logger.setLevel(logging.INFO)

name = ''
try:
    name = 'Name: {}'.format(os.environ['MY_POD_NAME'])
except Exception as e: 
    print e

@app.route('/')
def index():
    return render_template('index.html', name=name)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

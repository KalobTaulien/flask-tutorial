import datetime
from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/time')
def timetest():
    now = datetime.datetime.now()
    return render_template('time.html', now=now)


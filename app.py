# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request
from datetime import datetime
from model import getImageUrlFrom
import os

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", time = datetime.now())


@app.route('/yourgif', methods=['GET', 'POST'])
def yourgif():
    query = request.form['gifchoice']
    gif = getImageUrlFrom(request.form['gifchoice'])
    return render_template('yourgif.html', gif=gif, query=query)


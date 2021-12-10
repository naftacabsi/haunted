import flask
from flask import *

app = Flask('')

@app.route('/')
def main():
  return render_template("index.html")

@app.route('/whatishaunted')
def wih():
  return render_template("whatishaunted.html")

@app.route('/persik')
def persik():
  return render_template("persik.html")

@app.route('/vanirka')
def vanirka():
  return render_template("vanirka.html")

@app.route('/wtxil')
def wtxil():
  return render_template("wtxil.html")

@app.route('/ilya')
def ilya():
  return render_template("ilya.html")

@app.route('/deathkiller')
def death():
  return render_template("death.html")

@app.route('/steve')
def steve():
  return render_template("steve.html")

app.run('0.0.0.0', 2575)
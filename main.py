import flask
from flask import *

app = Flask('')

@app.route('/')
def main():
  return render_template("index.html")

app.run('0.0.0.0', 2575)
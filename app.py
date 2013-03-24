from flask import Flask
from flask import render_template


app = Flask(__name__)

app.debug = True


@app.route("/")
def home():
    return render_template('pages/home.html')

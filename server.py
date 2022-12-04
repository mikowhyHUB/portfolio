from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def my_portfolio():
    return render_template('index.html')

@app.route("/generic.html")
def generic():
    return render_template('generic.html')



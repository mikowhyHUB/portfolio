from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def my_portfolio():
    return render_template('index.html')


@app.route("/generic.html")
def generic():
    return render_template('generic.html')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    return 'form submited elo'

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def my_portfolio():
    return render_template('index.html')


@app.route("/favicon.ico")
def blog():
    return "This are my test of this server"


@app.route("/blog/2022/miso")
def blog2():
    return "This route is bout Miso"


@app.route("/about")
def about():
    return render_template('about.html')

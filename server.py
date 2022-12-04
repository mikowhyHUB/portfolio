from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def my_portfolio():
    return render_template('index.html')


@app.route("/generic.html")
def generic():
    return render_template('generic.html')


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        name = data['name']
        message = data['message']
        file = database.write(f'\n{email},{name},{message}')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        print(data)
        return redirect('/')
    else:
        return 'something went wrong'

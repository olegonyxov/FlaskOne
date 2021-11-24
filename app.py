from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    image = url_for('static', filename='flask-logo.png')
    return render_template("hello.html", name=image)
    # return f'<img src ="{image}"/> <br> index'


def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/login')
def login():
    return 'login'


@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'


with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

import datetime
import time
import uuid

from flask import Flask
from flask import render_template

app = Flask(__name__)


def make_resp_line():
    # a=1
    # b=2
    start = time.monotonic()
    datenow = datetime.datetime.now().strftime("%d-%m-%Y")
    timenow = datetime.datetime.now().strftime("%H:%M:%S")
    end = time.monotonic()
    respdelay = ":"+str(end - start)[0:4]+"s:"
    respuuid = str(uuid.uuid4())
    respline = respuuid + "\t" + respdelay + "\t" + datenow + "\t" + timenow
    return respline


@app.route('/get_data/<int:count>', methods=['GET'])
def index(count=1):
    resplist = []
    for i in range(count):
        resplist.append(make_resp_line())
    return render_template("get_data.html", rlist=resplist)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

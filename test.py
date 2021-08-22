import flask
from flask import request, jsonify
import time, math
import re
import json
from urllib.request import urlopen



app = flask.Flask(__name__)
app.config["DEBUG"] = True

def burn_cpu():
    '''
    Description:
        Burn Cpu for more than 1 sec

    '''    
    burning_sec = 1
    st_time = time.time()
    while True:
        if time.time() - st_time >= burning_sec:
            break
        else:
            math.factorial(100)



    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    data = json.load(response)

    IP=data['ip']
    org=data['org']
    city = data['city']
    country=data['country']
    region=data['region']

    return f"request completed {IP}  {org} {city} {country} {region}"


@app.route('/', methods=['GET'])
def home():
    return burn_cpu()


app.run(host='0.0.0.0')
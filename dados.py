import email
import json
import requests

def check_data():

    data = requests.get('email') 
    res = json.loads(data.json)

    output = [email]

    for data.json 
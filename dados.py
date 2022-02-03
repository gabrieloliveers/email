import email
import json
from tkinter import E
import requests

def check_data():

    data = requests.get('email') 
    res = json.loads(data.json)

    output = [email]


    data = email
    
    for d in data.json:
        for value in d.values():
            if value==email:
                print ('o email é: ', d['email'])
            
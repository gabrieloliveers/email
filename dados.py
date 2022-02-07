import email
import json
from msilib.schema import File

def check_data():

    with open('data.json') as json_file: 
        data = json.load(json_file) 

data = '{"nome": "Gabriel"; "data nascimento": "03/06/1999"; "email": "gr.oliveira99@gmail.com"}'

file = json.loads(data)

print(file['email']) 
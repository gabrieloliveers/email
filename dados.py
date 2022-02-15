import email
import json
from datetime import datetime

from main import send_email

# test = {}
# test["nome"] = "Alex"
# test["idate"] = 27
# test2 = {"nome": "Alex", "idade": 27}
# print(json.dumps(test)) # converte um dict em json

data_today = datetime.today()
data = data_today.strftime('%d/%m')
            
def check_data():
    with open('data.json') as json_file: 
        for line in json_file:
            user = json.loads(line)
            date_birthday = datetime.strptime(user["data_nascimento"], '%d/%m/%Y').date()
            niver = date_birthday.strftime('%d/%m')
            if data == niver:
                # print("é aniversário do {} que nasceu no dia {}".format(user["nome"], user["data_nascimento"]))
                send_email(user["email"])
                print(f'é aniversário do {user["nome"]} que nasceu no dia {user["data_nascimento"]}')
            else:
                print(f'não é aniversário do {user["nome"]} que nasceu no dia {user["data_nascimento"]}')
              

def is_birthday():
    with open('data.json') as json_file: 
        for line in json_file:
            user = json.loads(line)
            date_birthday = datetime.strptime(user["data_nascimento"], '%d/%m/%Y').date()
            niver = date_birthday.strftime('%d/%m')
            if data == niver:
               return user
            else:
               return None

check_data()

user = is_birthday()
if user:
    send_email(user["email"])
else:
    pass

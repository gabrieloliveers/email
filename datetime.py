#JEITO 1
from datetime import date

data_niver = "10/05/1988" 
current_date = date.today()
 
print("A idade é : ",current_date - data_niver)


#======================= TENTANDO SUBTRAIR OS DATETIMES E APANHANDO LEGAL KKKKK ====================================================

#JEITO 2
import json
from datetime import datetime, date

current_date = date.today

def idade(current_date, date_birthday):
    
    with open('data.json') as json_file: 
        for line in json_file:
            user = json.loads(line)
            date_birthday = datetime.strptime(user["data_nascimento"], '%d/%m/%Y').date()
    
            date_today = datetime.strptime(current_date, "%Y")
            date_niver = datetime.strptime(date_birthday, "%Y")
    
            print(date_today - date_niver)
    
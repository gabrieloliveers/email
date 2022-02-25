#JEITO 1
#from datetime import date

#data_niver = "10/05/1988" 
#current_date = date.today()
 
#print("A idade é : ",current_date - data_niver)


#======================= TENTANDO SUBTRAIR OS DATETIMES E APANHANDO LEGAL KKKKK ====================================================

#JEITO 2
import json
from datetime import datetime

current_date = datetime.today()

def idade(current_date):
    
    with open('data.json') as json_file: 
        for line in json_file:
            user = json.loads(line)
            date_birthday = datetime.strptime(user["data_nascimento"], '%d/%m/%Y').date()
            
            # niver = date_birthday.strftime('%d/%m/%Y')
            
            date_today = datetime.strftime(current_date, "%Y")
            date_niver = datetime.strftime(date_birthday, "%Y")
    
            print("A idade é:",int(date_today) - int(date_niver))

idade(current_date)

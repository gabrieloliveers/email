import smtplib
import email
import json



message = email.message.Message()

message['Subject'] = "Assunto"
message['From'] = 'gr.oliveira99@gmail.com'
message['To'] = 'alexsander.pereira@icloud.com' 
message.add_header('Content-Type', 'text/html')

with open("body.html", "r") as file_body:
        body = file_body.read()

message.set_payload(body)

password = 'senha' 

s = smtplib.SMTP('smtp.gmail.com: 587')

s.starttls()
s.login(message['From'], password)
s.sendmail(message['From'], [message['To']], message.as_string().encode('utf-8'))
    
print('Email enviado')

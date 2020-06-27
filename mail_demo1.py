import os
import smtplib

email_address = os.environ.get('DB_USER')
email_password = os.environ.get('DB_PASS')

message = """\
Subject: Testing 123

Hey, hows it going?

"""

reciever = email_address

server = smtplib.SMTP('smtp.gmail.com', 587) #Initialize server to establish a gmail (server adress) using port 587
server.starttls() #Starts the connection
server.login(email_address, email_password) #Login to the server
print("Login success") 
server.sendmail(email_address, reciever, message) #Send the email
print("Message sent!")

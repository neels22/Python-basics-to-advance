

# to send email 
# cononect to server confirm connection setting a protocol loggin on and then sending a message

# built in smtplib library makes these steps easy 

import smtplib

smtp_obj = smtplib.SMTP('smtp.gmail.com',587)

print(smtp_obj.ehlo())

print(smtp_obj.starttls())


import getpass

email = getpass.getpass('email : ')
password = getpass.getpass(' passwword please: ')
print(smtp_obj.login(email,password))


from_Address = email

to_add = email

subject = input('enter the subject: ')
message = input('ebter the message: ')
msg = 'Subject: '+subject+'\n'+message

print(smtp_obj.sendmail(from_Address,to_add,msg))

print(smtp_obj.quit())


# #################### receiving email from pyhton 


# import imaplib

# m = imaplib.IMAP4_SSL('imap.gmail.com')

# email = getpass.getpass('email : ')
# password = getpass.getpass(' passwword please: ')

# print(m.login(email,password))

# print(m.list())

# print(m.select('inbox'))

# typ,data = m.search(None,'BEFORE 01-N')





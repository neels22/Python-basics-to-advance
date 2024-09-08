
#################### receiving email from pyhton 


import imaplib
import getpass
import email


m = imaplib.IMAP4_SSL('imap.gmail.com')

email = getpass.getpass('email : ')
password = getpass.getpass(' passwword please: ')

print(m.login(email,password))

print(m.list())

print(m.select('inbox'))

typ,data = m.search(None,'SUBJECT "this is test 2"')

print(typ)
print(data)

email_id = data[0]

result , email_data = m.fetch(email_id,'(RFC822)')

#email data

raw_email = email_data[0][1]

raw_email_str = raw_email.decode('utf-8')

email_message = email.message_from_string(raw_email_str)

for part in email_message.walk():
    if part.get_content_type() =='text/plain':
        body = part.get_payload(decode = True)
        print(body)







import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html ').read_text())
email = EmailMessage()
email['from'] = 'Nikolay Rudenko'
email['to'] = 'nikolayrudenko1@gmail.com'
email['subject'] = 'Hello, how are you!'

email.set_content(html.substitute(name='This is my message'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    # connect to SMTP server into TLS mode
    smtp.starttls()
    smtp.login('*****@gmail.com', '*******')
    smtp.send_message(email)
    print('All good boss!')
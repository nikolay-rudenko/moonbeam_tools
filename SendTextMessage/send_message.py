from twilio.rest import Client

account_sid = '***'
auth_token = '***'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='whatsapp:***',
    body='Hello from python!',
    to='whatsapp:***'
)

print(message.sid)
from twilio.rest import Client

account_sid = 'ACa1c90d8ac0ff3b14602e7c2cb19d9ab8'
auth_token = '1146eb3539517867ca0f1ce51f71d440'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='whatsapp:+14155238886',
    body='Hello from python!',
    to='whatsapp:+380638768742'
)

print(message.sid)
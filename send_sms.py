#install Twilio in the Env via pip install twilio

from twilio.rest import Client


# Your Account Sid  and Auth Token from Twilio.com/user/account
account_sid = "#"
auth_token = "#"
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="\nHello World, I have sent this message via my Code.", #Replace with your phone number
    to="#‬",  #Replace with your twilio phone number ‭+491607508824
    from_="#")
print(message.sid)



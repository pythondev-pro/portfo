
import os
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
# To set up environmental variables, see http://twil.io/secure
account_sid ='ACae9769983f5f1dcc40e982199b54bb95'
auth_token = '37eb50ff51924d65e54d0ecfac54e588'
# best practice
# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']

client = Client(account_sid, auth_token)

message = client.api.account.messages.create(
    to="+number",
    from_="+number",
    body="Great work! Click www.lepetitlivre.org")
    
print(message.sid)

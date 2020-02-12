from twilio.rest import Client 
 
account_sid = 'AC1771278163148e0395e665ec36cf35d5' 
auth_token = 'd968b840a4a6c8ca19808034df1fba08' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='+19182129502',  
                              body='Hello',      
                              to='+60163066883' 
                          ) 
 
print(message.sid)

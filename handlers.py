from flask import request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import os

# Your Twilio account SID and auth token
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

# A dictionary to store user states
user_states = {}

def whatsapp_reply():
    # Get the message body from the request
    message_body = request.values.get('Body', '')
    # Get the sender's phone number
    from_number = request.values.get('From', '')

    # ... rest of your code ...

    # Create a response
    resp = MessagingResponse()

    # Add a message to the response
    resp.message(response_message)

    return str(resp)

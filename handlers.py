from flask import request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()
from .registration import handle_registration
from .ordering import handle_order
from .referral import handle_referral

# Your Twilio account SID and auth token
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)


# A dictionary to store user states
user_states = {}



def whatsapp_reply():
    # Get the message body from the request
    message_body = request.values.get('Body', '')

    print("Body is: " +message_body)  
    

    # Get the sender's phone number
    from_number = request.values.get('From', '')
    print("Number is: "+ from_number)  

    # Check if the user is already in a conversation

    if from_number not in user_states or message_body == 'hi':
        # If not, start a new conversation
        user_states[from_number] = 'MENU'
        response_message = "Hello! Here are your options:\n1. Register\n2. Place order\n3. Get referral code"
    else:
        # If so, continue the conversation
        if user_states[from_number] == 'MENU':
            if message_body =='1':
                user_states[from_number] = 'REGISTER'
                response_message = "You've selected 'Register'. Please provide your name."
            elif message_body == '2':
                user_states[from_number] = 'ORDER'
                response_message = "You've selected 'Place order'. Please provide your order details."
            elif message_body == '3':
                user_states[from_number] = 'REFERRAL'
                response_message = "You've selected 'Get referral code'. Here is your referral code: XXXX."
            else:
                response_message = "Invalid option. Please select 1, 2, or 3."
        elif user_states[from_number] == 'REGISTER':
           #handle registration
           response_message = handle_registration(message_body, from_number)
                    
        elif user_states[from_number] == 'ORDER':
            # Handle order...
            response_message = handle_order(message_body, from_number)
        elif user_states[from_number] == 'REFERRAL':
            # Handle referral...
            response_message = handle_referral(message_body, from_number)

    # Create a response
    resp = MessagingResponse()

    # Add a message to the response
    resp.message(response_message)

    return str(resp)








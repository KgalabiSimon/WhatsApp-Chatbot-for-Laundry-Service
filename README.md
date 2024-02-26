# Project Title: WhatsApp Chatbot for Student Laundry Service

## Description
This project is a WhatsApp chatbot designed to facilitate the operations of a student-based laundry service. The chatbot is built using Flask and the Twilio API, and it provides a convenient interface for users to interact with the service via WhatsApp.

## Features
The chatbot provides the following features:

1. **User Registration**: Users can register with the service by providing their name, surname, and residence. The chatbot guides the user through the registration process by asking for each piece of information in turn.

2. **Order Placement**: Users can place laundry orders through the chatbot. When a user selects this option, the chatbot provides a price list for the laundry services and asks for the order details.

3. **Referral Code Retrieval**: Users can retrieve their referral code through the chatbot. This feature is designed to facilitate the service's referral program.

## Implementation
The chatbot uses a simple state machine to keep track of the current state of the conversation for each user. When a new message is received, the chatbot checks the user's current state and responds accordingly. The user's state is updated after each message.

## Future Work
Future work on this project could include adding more features to the chatbot, such as order tracking, payment processing, and customer support. Additionally, the chatbot could be integrated with a database to store user information and order details.

## Disclaimer
This project is a basic example and doesn't include any error handling, security measures, or actual database operations. These features would need to be added before using this in a production environment.

## Getting Started
To get started with this project, you'll need a Twilio account and a Flask development environment. You'll also need to set up a webhook in your Twilio account to point to the `/whatsapp` endpoint in this Flask app to receive incoming messages. You can do this in the [Twilio Console](https://www.twilio.com/console). Please replace `account_sid`, `auth_token`, and `twilio_phone_number` in the code with your actual Twilio account SID, auth token, and phone number.

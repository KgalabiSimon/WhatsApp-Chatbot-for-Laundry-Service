from flask import Flask
from dotenv import load_dotenv
import os
from handlers import whatsapp_reply

load_dotenv()  # take environment variables from .env.

app = Flask(__name__)

app.route("/whatsapp", methods=['POST'])(whatsapp_reply)

if __name__ == "__main__":
    app.run(debug=True)

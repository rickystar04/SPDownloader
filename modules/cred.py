import os

from dotenv import load_dotenv

load_dotenv()

client_ID = os.getenv("client_ID")
client_SECRET = os.getenv("client_SECRET")
redirect_url = os.getenv("redirect_url")

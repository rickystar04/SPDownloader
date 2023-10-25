from dotenv import load_dotenv
import os

def verify_credential():
    load_dotenv()

    client_ID = os.getenv("client_ID")
    client_SECRET = os.getenv("client_SECRET")
	
    if(client_ID=="" and client_SECRET==""):
        print("Client ID and Client Secret not present")
        print("Follow the instructions in the README.md file to obtain your credentials")
    
    elif (client_ID==""):
        print("Client ID not present")
        print("Follow the instructions in the README.md file to obtain your credentials")

    elif(client_SECRET==""):
        print("Client Secret not present")
        print("Follow the instructions in the README.md file to obtain your credentials")
    

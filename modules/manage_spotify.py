import cred
from spotify import *

if(cred.client_ID=="" and cred.client_SECRET==""):
	print("Client ID and Client Secret not present")
	print("Follow the instructions in the README.md file to obtain your credentials")
elif (cred.client_ID==""):
	print("Client ID not present")
	print("Follow the instructions in the README.md file to obtain your credentials")
	
elif(cred.client_SECRET==""):
	print("Client Secret not present")
	print("Follow the instructions in the README.md file to obtain your credentials")

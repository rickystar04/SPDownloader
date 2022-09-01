
import cred
from spotify import *

if(cred.client_ID=="" and cred.client_SECRET==""):
	print("Client ID e  Client Secret non presenti")
	print("Segui le istruzioni presenti nel file README.md per ottenere le tue credenziali")
elif (cred.client_ID==""):
	print("Client ID non presente")
	print("Segui le istruzioni presenti nel file README.md per ottenere le tue credenziali")
	
elif(cred.client_SECRET==""):
	print("Client Secret non presente")
	print("Segui le istruzioni presenti nel file README.md per ottenere le tue credenziali")

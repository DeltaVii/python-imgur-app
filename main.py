##############################
##                          ##
## Kelly Norris             ##
##                          ##
## Pymgus Lang Imgur Client ##
##                          ##
## Semester 2, 2017         ##
##                          ##
##############################

#Importing API package
from imgurpython import ImgurClient
#Networking imports
from pprint import pprint
import requests
import json
import webbrowser
#Image handling imports (idk what for)
import base64

#Inputting App IDs
client_id = '16bb853579ca0a9'
client_secret = '93425782251b67c7254c46869e6be8b3c2c03e7a'

#Creating Client var
client = ImgurClient(client_id, client_secret)

def gallery_check():
    items = client.gallery()
    for item in items:
        print(item.link)

def upload_anon():
    fpath = input("input filepath")
    client.upload_from_path(fpath)
    return 

print("What would you like to do? \ninput i for gallery items\ninput u for upload")
print("Input 'auth' to authorize your account for user uploads")
user_input = input()
if user_input == "i":
    gallery_check()
if user_input == "auth":
    authorization_url = client.get_auth_url('pin')
    webbrowser.open_new_tab(authorization_url)
    print('input pin')
    pin = input()
    #   PYTHON LET ME GET THE FUCKING PIN JESUS CHRIST
    #   thank you
    credentials = client.authorize('FUCK MY ASS', grant_type='pin')
    print(credentials)
    #client.set_user_auth(credentials['access_token'], credentials['refresh_token'])
    
#testing -- under construction



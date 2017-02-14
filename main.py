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
#some anonymous functions
def gallery_check():
    items = client.gallery()
    for item in items:
        print(item.link)

def upload_anon():
    fpath = input("input filepath")
    client.upload_from_path(fpath)
    
#the Authorization class
#everything that uses a user auth comes from this
class Auth2:
    #setting variables needed for authentication
    pin = ""
    access_token = ""
    refresh_token = ""
    
    #This function opens a web page, and the user needs to log in
    #Once they log in and authorize the app, they get a pin
    #The pin needs to be pasted back into the shell
    def getPin(self, client_id, client_secret):
        resp = "pin"
        state = "succ"
        authorization_url = client.get_auth_url('pin')
        webbrowser.open_new_tab(authorization_url)
        self.pin = input("paste pin here\n")

    #This function exchanges the pin for an access and refresh token
    def pinTokenExchange(self, client_id, client_secret, pin):
        params ={"client_id" : client_id,
                 "client_secret" : client_secret,
                 "grant_type" : "pin",
                 "pin" : self.pin}

        url = r"https://api.imgur.com/oauth2/token/"
        r = requests.post(url, data = params, verify = True)

        j = r.json()
        print("The pinTokenExchange response:")
        print(self.pin)
        
        #debug print
        print(j)

        self.access_token = j['access_token']
        self.refresh_token = j['refresh_token']
        print ("Access Token: ",self.access_token,"\nRefresh Token: ",self.refresh_token)

    #This function allows an authenticated user to upload to their account from a url
    def uploadFromURL(self, access_token):
        image_url = input("Input url of image you want to upload\n")
        image_title = input("Input title of image\n")

        headers = {"authorization":"Bearer {0}".format(access_token)}

        upload_url = r'https://api.imgur.com/3/upload'

        payload = {"image": image_url,
                   "type": 'url',
                   'title': image_title}

        r = requests.post(upload_url, data=payload, headers=headers, verify=True)

        j = r.json()
        print("Uploader response:")
        print(j)

        uploaded_url = j['data']['link']
        print("The uploaded image URL is: ", uploaded_url)
    
#making instance of Auth2
auth2 = Auth2()

#initial input 
print("What would you like to do? \ninput i for gallery items")
print("Input 'auth' to authorize your account for user uploads")
user_input = input()
if user_input == "i":
    gallery_check()

if user_input == "auth":
    auth2.getPin(client_id, client_secret)
    auth2.pinTokenExchange(client_id, client_secret, pin)

    #Past this point is authenticated user actions
    user_input = input("""
    Your account is now authorized.\n
    What would you like to do?\n
    Type "url" to upload from a URL.\n
    """)
    if user_input == "url":
        auth2.uploadFromURL(auth2.access_token)




    



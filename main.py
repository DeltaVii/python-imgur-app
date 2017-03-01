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
from imgurpython import *
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

##Testing Zone##




#Anonymous class
class Anon:
    anon_actions = []

    #Gallery check
    anon_actions.append("gallery check")
    def gallery_check(self):
        items = client.gallery()
        for item in items:
            print(item.link)
        self.anon_loop()

    #Better gallery check?
    anon_actions.append("gallery check 2")
    def gallery_check2(self):
        section = input("Input hot, top or user")
        sort = input("Input viral or time")
        window = None
        show_viral = None
        if section == "top":
            window = input("Input day, week, month, year or all")
        if section == "user":
            show_viral = input("Input true or false for viral images")
        limit = input("Input limit for images, None for no limit")
        client.gallery(section=section,sort=sort,window=window,show_viral=show_viral,limit=limit)
    

    #Anon upload
    anon_actions.append("anon upload")
    def upload_anon(self):
        fpath = input("input filepath")
        client.upload_from_path(fpath)
        self.anon_loop()

    #Loop for the actions
    def anon_loop(self):
        print("\n\n\n")
        for i in range(len(self.anon_actions)):
            print(self.anon_actions[i])
        anon_input = input("Input your action choice from the list above\n")

        if anon_input == "gallery check":
            self.gallery_check()
        elif anon_input == "anon upload":
            self.upload_anon()
        elif anon_input == "quit":
            runProgram(anon,auth2)
        elif anon_input == "gallery check 2":
            self.gallery_check2()
        self.anon_loop()





    
#the Authorization class
#everything that uses a user auth comes from this
class Auth2:
    #setting variables needed for authentication
    pin = ""
    access_token = ""
    refresh_token = ""

    auth_actions = []
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

    #Authentication function
    def authentication(self):
        self.getPin(client_id, client_secret)
        self.pinTokenExchange(client_id, client_secret, self.pin)
        self.auth_loop()



    
    #This function allows an authenticated user to upload to their account from a url
    auth_actions.append("URL Upload")
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


    def auth_loop(self):
        print("\n\n\n")
        for i in range(len(self.auth_actions)):
            print(self.auth_actions[i])

        auth_input = input("Input your action choice from the list above\n")

        if auth_input == "URL Upload":
            self.uploadFromURL()
            self.auth_loop()
        elif auth_input == "Get User":
            self.get_user()
        elif auth_input == "quit":
            runProgram(anon,auth2)
        else:
            self.auth_loop()

    auth_actions.append("Get User")
    def get_user(self):
        params = {"client_id" : client_id}
        r = requests.get("https://api.imgur.com/3/account/DeltaViii", data=params)
        print(r)
        j = r.json
        print(j)
        client.get_account("me")
        self.auth_loop()



#making instances of classes
anon = Anon()
auth2 = Auth2()


#initial input
def runProgram(anon, auth2):
    print("Welcome to Pymgus Lang Imgur client.")
    user_input = input("""
    Input whether you want to do anonymous actions or user-based actions.\n
    Type "anon" for anonymous actions\n
    Type "auth" to authorize your Imgur account and do user-based actions\n
    Input "quit" at any input to return to the beginning\n
    """)

    if user_input == "anon":
        anon.anon_loop()

    if user_input == "auth":
        auth2.authentication()

runProgram(anon, auth2)
    



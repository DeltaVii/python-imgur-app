#Testing file for the other python imgur library, PyImgur


import pyimgur
import webbrowser

CLIENT_ID = '16bb853579ca0a9'
CLIENT_SECRET = '93425782251b67c7254c46869e6be8b3c2c03e7a'

client = pyimgur.Imgur(CLIENT_ID, CLIENT_SECRET)

class Anon:
    anon_actions = []
    
    def anon_loop(self):
        for i in len(range(self.anon_actions)):
            print(self.anon_actions[i])
        anon_input = input("Choose from the list above")

class Auth:
    #making list of actions
    auth_actions = []

    #getting user authorizations
    def authorization(self):
        auth_url = client.authorization_url('pin')
        webbrowser.open(auth_url)
        pin = input("Paste pin here:")

        client.exchange_pin(pin)

        self.auth_loop()

    #the Get User function
    #involves looking up users
    auth_actions.append("Get User")
    def get_user(self):
        #getting username input
        username = input("Input username to get:")
        if username == "back":
            self.auth_loop()
        #creates a User object with username
        user = client.get_user(username)
        print("usernmae is:",user.name)
        print("Bio:",user.bio)
        print("User ID:",user.id)
        print("User Rep:",user.reputation)
        
        #asking for more actions
        get_user_input = input("Would you like to do user actions? y/n:")
        if get_user_input == "n":
            self.auth_loop()
        elif get_user_input == "y":
            get_user_actions = []

            #listing out actions
            get_user_actions.append("Get Albums")
            get_user_actions.append("Get Comments")
            get_user_actions.append("Get Favorites")
            get_user_actions.append("Get Gallery Favorites")
            get_user_actions.append("Get Gallery Profile")
            get_user_actions.append("Get Statistics")
            get_user_actions.append("Get Images")
            get_user_actions.append("Send Message")

            for i in range(len(get_user_actions)):
                print(get_user_actions[i])


            #User actions input
            get_user_actions_input = input("Choose from the above list:")

            #If statements in reply
            #Albums
            if get_user_actions_input == "Get Albums":
                result = user.get_albums(limit=None)
                for i in range(len(result)):
                    print(result[i].link)
                self.auth_loop()
            #Comments
            elif get_user_actions_input == "Get Comments":
                result = user.get_comments()
                for i in range(len(result)):
                    print(i, ") ",result[i].text, "\n", sep='')
                self.auth_loop()
            #Favorites
            elif get_user_actions_input == "Get Favorites":
                result = user.get_favorites()
                for i in range(len(result)):
                    print(result[i].link)
                self.auth_loop()
            #Gallery Favorites
            elif get_user_actions_input == "Get Gallery Favorites":
                result = user.get_gallery_favorites()
                for i in range(len(result)):
                    print(result[i].link)
                self.auth_loop()
            #Gallery Profile
            elif get_user_actions_input == "Get Gallery Profile":
                result = user.get_gallery_profile()
                print(result)
                self.auth_loop()
            #Stats
            elif get_user_actions_input == "Get Statistics":
                result = user.get_statistics()
                print(result)
                self.auth_loop()
            #Images
            elif get_user_actions_input == "Get Images":
                result = user.get_submissions()
                for i in range(len(result)):
                    print(result[i].link)
                self.auth_loop()
            #Message
            elif get_user_actions_input == "Send Message":
                body = input("Input body of message:")
                subject = input("Input subject of message:")
                send_message(body, subject, reply_to=None)
                self.auth_loop()

            #go backs
            elif get_user_actions_input == "back":
                self.auth_loop()
            else:
                print("Input not understood")
                self.get_user()
    
    def auth_loop(self):
        for i in range(len(self.auth_actions)):
            print(self.auth_actions[i])
        auth_input = input("Choose from the list above")
        if auth_input == "Get User":
            self.get_user()
        #go back to the original input
        elif auth_input == "back":
            user_input = input("Anon or Auth?\n")
            if user_input == "Anon":
                anon.anon_loop
            elif user_input == "Auth":
                auth.authorization()
        else:
            auth_loop()
        
anon = Anon()
auth = Auth()
user_input = input("Anon or Auth?\n")
if user_input == "Anon":
    anon.anon_loop
elif user_input == "Auth":
    auth.authorization()


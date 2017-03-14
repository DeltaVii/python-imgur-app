#Testing file for the other python imgur library, PyImgur


import pyimgur
import webbrowser

CLIENT_ID = '16bb853579ca0a9'
CLIENT_SECRET = '93425782251b67c7254c46869e6be8b3c2c03e7a'

client = pyimgur.Imgur(CLIENT_ID, CLIENT_SECRET)

class Anon:
    anon_actions = []
    
    
    #Gallery lister
    anon_actions.append("Gallery Viewer")
    def anon_gallery(self):
        #Getting preferences for section
        section = input("Input 'hot', 'top', or 'user':").lower()
        #making sure the input works
        if section != "hot" and section != "top" and section != "user":
            print("Input not understood, defaulting to 'hot'")
            section = "hot"
        #Getting preferences for sorting
        sort = input("Input 'viral' or 'time':").lower()
        #making sure the input works
        if sort != "viral" and sort != "time":
            print("Input not understood, defaulting to 'viral'")
            sort = 'viral'

        #creating result variable from preferences
        result = client.get_gallery(section = section, sort = sort, limit=100)
        #printing result with number list
        for i in range(len(result)):
            print(i+1, ")", end='', sep='')
            print(result[i].link)
        #Asking for link opening
        link_get_bool = input("Want to open any link? y/n:")
        if link_get_bool == "y":
            #making a while loop for opening multiple links
            get_links = True
            while get_links == True:
                #Getting input of the number for the link
                link_get_number = input("Input the number that you want: ")
                #making input an integer
                int(link_get_number)
                #Opening with webbrowser
                #result list; index number is the input minus 1's link object
                #.link makes sure to get a link and not the album/image object
                webbrowser.open(result[int(link_get_number) - 1].link)

                #Asking for a repeat
                link_get_repeat = input("Would you like to open another? y/n: ")
                if link_get_repeat == "y".lower():
                    pass
                elif link_get_repeat == "n".lower():
                    get_links = False
                else:
                    print("Input not understood, returning to anon_loop")
                    self.anon_loop()
            #ending link get loop
            self.anon_loop()
            
        #ending whole loop
        elif link_get_bool == "n":
            self.anon_loop()
        else:
            self.anon_loop()
    #### End of Gallery Getter ####

    #Anon loop for anonymous actions
    def anon_loop(self):
        #Printing list of actions with numbers
        for i in range(len(self.anon_actions)):
            print(i+1,")", end='', sep='')
            print(self.anon_actions[i])
        #Getting user input for anon action
        anon_input = input("Choose from the list above: ")
        #Gallery  Viewer
        if anon_input =="Gallery Viewer".lower() or anon_input == "1":
            self.anon_gallery()
            
        #goback option
        elif anon_input == "back":
            user_input = input("Anon or Auth?\n").lower()
            if user_input == "anon":
                anon.anon_loop
            elif user_input == "auth":
                auth.authorization()
        else:
            self.anon_loop()
        
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


    auth_actions.append("Message User")
    def message(self):
        #getting username input
        username = input("Input username to get:")
        if username == "back":
            self.auth_loop()
        #creates a User object with username
        user = client.get_user(username)
        body = input("Input the body of your message: ")
        subject = input("Input the subject of your message: ")

        user.send_message(body,subject,reply_to=None)
        self.auth_loop()
    
    def auth_loop(self):
        for i in range(len(self.auth_actions)):
            print(self.auth_actions[i])
        auth_input = input("Choose from the list above")
        if auth_input == "Get User":
            self.get_user()
        #go back to the original input
        elif auth_input == "back":
            user_input = input("Anon or Auth?\n").lower()
            if user_input == "anon":
                anon.anon_loop
            elif user_input == "auth":
                auth.authorization()
        else:
            auth_loop()

#creating instances of the classes
anon = Anon()
auth = Auth()
user_input = input("Anon or Auth?\n").lower()
if user_input == "anon":
    anon.anon_loop()
elif user_input == "auth":
    auth.authorization()


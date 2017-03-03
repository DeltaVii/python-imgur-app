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
    auth_actions = []

    def authorization(self):
        auth_url = client.authorization_url('pin')
        webbrowser.open(auth_url)
        pin = input("Paste pin here:")

        client.exchange_pin(pin)

        self.auth_loop()

    auth_actions.append("Get User")
    def get_user(self):
        username = input("Input username to get:")
        user = client.get_user(username)
        print("usernmae is:",user.name)
        print("Bio:",user.bio)
        print("User ID:",user.id)
        print("User Rep:",user.reputation)

        get_user_input = input("Would you like to do user actions? y/n:")
        if get_user_input == "n":
            self.auth_loop()
        elif get_user_input == "y":
            get_user_actions = []

            get_user_actions.append("Get Albums")
            get_user_actions.append("Get Comments")
            get_user_actions.append("Get Favorites")
            get_user_actions.append("Get Gallery Favorites")
            get_user_actions.append("Get Gallery Profile")
            get_user_actions.append("Get Images")
            get_user_actions.append("Get Messages")
            get_user_actions.append("Get Notifications")
            get_user_actions.append("Get Statistics")
            get_user_actions.append("Get Submissions")
            get_user_actions.append("Check Email Verification")

            for i in range(len(get_user_actions)):
                print(get_user_actions[i])

            get_user_actions_input = input("Choose from the above list:")
            if get_user_actions_input == "Get Albums":
                result = user.get_albums(limit=None)
                print(result)
            elif get_user_actions_input == "Get Comments":
                result = user.get_comments()
                for i in range(len(result)):
                    print(i, ") ",result[i].text, "\n", sep='')
            elif get_user_actions_input == "Get Favorites":
                result = user.get_favorites()
                print(result)
    
    def auth_loop(self):
        for i in len(range(aelf.auth_actions)):
            print(self.auth_actions[i])
        auth_input = input("Choose from the list above")
        if auth_input == "Get User":
            self.get_user()
        else:
            auth_loop()
        
anon = Anon()
auth = Auth()
user_input = input("Anon or Auth?\n")
if user_input == "Anon":
    anon.anon_loop
elif user_input == "Auth":
    auth.authorization()


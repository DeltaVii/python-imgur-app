from kivy.app import App
from kivy.uix.button import Button

#Kivy functions#
#layouts
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
#uix
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
#screen
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.properties import StringProperty

#imgur imports
import pyimgur
import webbrowser
#imgur vars
CLIENT_ID = '16bb853579ca0a9'
CLIENT_SECRET = '93425782251b67c7254c46869e6be8b3c2c03e7a'
client = pyimgur.Imgur(CLIENT_ID, CLIENT_SECRET)


#declaring function variables
section = ''
sort = ''
result = ''
result_list = []

Builder.load_string("""
<TitleScreen>:
    BoxLayout:
        orientation:'vertical'
        Image:
            source:'img/imgurlogo.png'
            size_hint_y:'.5'
            
            
        BoxLayout:
            Button:
                text:'Anonymous functions'
                background_color:(1,1,1,1)
                font_size:20
                on_press: root.manager.current = 'anon1'
                    
            Button:
                text:'Authorized functions'
                background_color:(1,1,1,1)
                font_size:20
                on_press: root.manager.current = 'auth_auth'
                
                
<AnonFunctions_1>:
    on_enter: root.clearVars()
    BoxLayout:
        orientation:'vertical'
        Label:
            text:'Anonymous Functions'

        BoxLayout:
            Button:
                text:'Gallery Getter'
                on_press: root.manager.current='anon_gallery1'
            Button:
                text:'Go Back'
                on_press: root.manager.current='title'

<AnonFunctions_Gallery1>:
    BoxLayout:
        orientation:'vertical'
        Label:
            text:'Choose a section'
        BoxLayout:
            Button:
                text:'hot'
                on_press: root.sectionHot()
                on_press: root.manager.current = 'anon_gallery2'
            Button:
                text:'top'
                on_press: root.sectionTop()
                on_press: root.manager.current = 'anon_gallery2'
            Button:
                text:'user'
                on_press: root.sectionUser()
                on_press: root.manager.current = 'anon_gallery2'

<AnonFunctions_Gallery2>:
    BoxLayout:
        orientation:'vertical'
        Label:
            text:'Choose a sort option'
        BoxLayout:
            Button:
                text:'viral'
                on_press: root.sortViral()
                on_press: root.manager.current = 'anon_gallery3'
                
            Button:
                text:'time'
                on_press: root.sortTime()
                on_press: root.manager.current = 'anon_gallery3'
                

<AnonFunctions_Gallery3>:
    on_enter: root.updateText()
    BoxLayout:
        TextInput:
            text: root.updated_text
                
        Button:
            text:'Go back'
            on_press: root.manager.current = 'anon1'
            

<Auth_1>:
    BoxLayout:
        orientation: 'vertical'
        TextInput:
            id: ti
            multiline: 'false'
            text: 'paste pin here, then press enter'
            on_text_validate: root.auth(ti.text)
        Button:
            text: 'Click here to open window and log in to imgur'
            on_press: root.open_window()

        Button:
            text: 'press me for auth because bleeehhh'
            on_press: root.auth(ti.text)
            on_press: root.manager.current = 'auth1'

<AuthFunctions_1>:
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'Get User function'
            on_press: root.manager.current = 'auth_getuser1'
        Button:
            text: 'Messenger function'
            on_press: root.manager.current = 'auth_message1'

<AuthFunctions_GetUser_1>:
    Button:
        text: 'go back'
        on_press: root.manager.current = 'auth1'
<AuthFunctions_Message_1>:
    Button:
        text: 'go back'
        on_press: root.manager.current = 'auth1'

""")

#Declaring screens
class TitleScreen(Screen):
    pass

class AnonFunctions_1(Screen):
    def clearVars(self):
        result_list = []
        
        

class AnonFunctions_Gallery1(Screen):
    #functions for different section selections
    def sectionHot(self):
        section = "hot"
        result_list.append(section)
        ##Delete for final
        print(result_list)
        print(section)
    def sectionTop(self):
        section = "top"
        result_list.append(section)
        ##Delete for final
        print(result_list)
        print(section)
    def sectionUser(self):
        section = "user"
        result_list.append(section)
        ##Delete for final
        print(result_list)
        print(section)

class AnonFunctions_Gallery2(Screen):
    def sortViral(self):
        sort = "viral"
        result_list.append(sort)
        ##Delete for final
        print(result_list)
        print(sort)
    def sortTime(self):
        sort = "time"
        result_list.append(sort)
        ##Delete for final
        print(result_list)
        print(sort)

class AnonFunctions_Gallery3(Screen):
    updated_text = StringProperty()

    def updateText(self):
        result = client.get_gallery(section = result_list[0], sort = result_list[1], limit = 20)
        chunks = []
        for i in range(len(result)):
            link = result[i].link
            chunks.append(link)
            chunks.append("\n")
        new_result = ''.join(chunks)
        #self.updated_text = result
        print('updateText has fired')
        print(result_list)
        print(result)
        print(new_result)
        self.updated_text = new_result
        if result == '':
            print("Result did not update")
        result = ''
        del result_list[:]
    
    

class Auth_1(Screen):
    def auth(self, ti):
        client.exchange_pin(ti)
        print('authorization has fired')

    def open_window(self):
        auth_url = client.authorization_url('pin')
        webbrowser.open(auth_url)

        
class AuthFunctions_1(Screen):
    pass

class AuthFunctions_GetUser_1(Screen):
    pass

class AuthFunctions_Message_1(Screen):
    pass



    

sm = ScreenManager(transition=NoTransition())
sm.add_widget(TitleScreen(name='title'))
sm.add_widget(AnonFunctions_1(name='anon1'))
sm.add_widget(AnonFunctions_Gallery1(name='anon_gallery1'))
sm.add_widget(AnonFunctions_Gallery2(name='anon_gallery2'))
sm.add_widget(AnonFunctions_Gallery3(name='anon_gallery3'))

sm.add_widget(Auth_1(name='auth_auth'))
sm.add_widget(AuthFunctions_1(name='auth1'))
sm.add_widget(AuthFunctions_GetUser_1(name='auth_getuser1'))
sm.add_widget(AuthFunctions_Message_1(name='auth_message1'))






class TestApp(App):
    def build(self):
        return sm
        


if __name__=="__main__":
    TestApp().run()

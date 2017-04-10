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
                
                
<AnonFunctions_1>:
    BoxLayout:
        orientation:'vertical'
        Label:
            text:'Anonymous Functions'
        Button:
            text:'Gallery Getter'
            on_press: root.manager.current='anon_gallery1'

<AnonFunctions_Gallery1>:
    BoxLayout:
        orientation:'vertical'
        Label:
            text:'Choose a section'
        BoxLayout:
            Button:
                text:'hot'
                on_press: section='hot'
                on_press: root.manager.current = 'anon_gallery2'
            Button:
                text:'top'
                on_press: section='top'
                on_press: root.manager.current = 'anon_gallery2'
            Button:
                text:'user'
                on_press: section='user'
                on_press: root.manager.current = 'anon_gallery2'

<AnonFunctions_Gallery2>:
    BoxLayout:
        orientation:'vertical'
        Label:
            text:'Choose a sort option'
        BoxLayout:
            Button:
                text:'viral'
                on_press: sort='viral'
                on_press: root.manager.current = 'anon_gallery3'
                
            Button:
                text:'time'
                on_press: sort='time'
                on_press: root.manager.current = 'anon_gallery3'
                

<AnonFunctions_Gallery3>:
    
    BoxLayout:
        AnonFunctions_Gallery3_Label:
            Label:
                text:'Kivy can suck my dick'
        Button:
            text:'Update because kivy is bad'
            
""")

#Declaring screens
class TitleScreen(Screen):
    pass

class AnonFunctions_1(Screen):
    pass

class AnonFunctions_Gallery1(Screen):
    pass

class AnonFunctions_Gallery2(Screen):
    pass

class AnonFunctions_Gallery3(Screen):
    pass
    
class AnonFunctions_Gallery3_Label(Widget):
    def updateText(self):
        self.Label.text = result
    

sm = ScreenManager(transition=NoTransition())
sm.add_widget(TitleScreen(name='title'))
sm.add_widget(AnonFunctions_1(name='anon1'))
sm.add_widget(AnonFunctions_Gallery1(name='anon_gallery1'))
sm.add_widget(AnonFunctions_Gallery2(name='anon_gallery2'))
sm.add_widget(AnonFunctions_Gallery3(name='anon_gallery3'))







class TestApp(App):
    def build(self):
        return sm
        


if __name__=="__main__":
    TestApp().run()

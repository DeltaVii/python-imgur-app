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
                on_press: root.sectionHot()
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
                on_press: root.sortViral()
                on_press: root.manager.current = 'anon_gallery3'
                
            Button:
                text:'time'
                on_press: sort='time'
                on_press: root.manager.current = 'anon_gallery3'
                

<AnonFunctions_Gallery3>:
    on_enter: root.updateText()
    BoxLayout:
        TextInput:
            text: root.updated_text
                
        Button:
            text:'This button is no longer needed'
            on_press: root.updateText()
            
            
""")

#Declaring screens
class TitleScreen(Screen):
    pass

class AnonFunctions_1(Screen):
    pass

class AnonFunctions_Gallery1(Screen):
    def sectionHot(self):
        section = "hot"
        result_list.append(section)
        print(result_list)
        print(section)

class AnonFunctions_Gallery2(Screen):
    def sortViral(self):
        sort = "viral"
        result_list.append(sort)
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
    
class AnonFunctions_Gallery3_Label(Widget):
    pass
    

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

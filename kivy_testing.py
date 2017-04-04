from kivy.app import App
from kivy.uix.button import Button

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition

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
                    
            Button:
                text:'Authorized functions'
                
        
""")

class TitleScreen(Screen):
    pass

sm = ScreenManager(transition=NoTransition())
sm.add_widget(TitleScreen(name='title'))

class TestApp(App):
    def build(self):
        return sm
        

if __name__=="__main__":
    TestApp().run()

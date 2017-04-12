from kivy.properties import StringProperty


import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.label import Label



Builder.load_string("""
<YourWidget>:
    BoxLayout:
        size: root.size
        Button:
            id: button1
            text: "Change text"
            on_release: root.change_text()
        Label:
            id: label1
            text: root.random_number


""")


class YourWidget(Widget):
    random_number = StringProperty()

    def __init__(self, **kwargs):
        super(YourWidget, self).__init__(**kwargs)
        self.random_number = str(random.randint(1, 100))
        print("init has happened")

    def change_text(self):
        self.random_number = str(random.randint(1, 100))
        print("Change text function has happened")

class YourApp(App):
    def build(self):
        return YourWidget()

if __name__ == '__main__':
    YourApp().run()

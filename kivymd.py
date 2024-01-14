from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.utils import *


class SayHello(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        
        self.window.add_widget(Image(source = "logo.png"))
        self.window.add_widget(Label(text="Welcome to our EMS App",font_size=30,
            color=get_color_from_hex('#00FF00'),  # Green color
            bold=True,))
        
        return self.window
    
if __name__ == "__main__":
    SayHello().run()
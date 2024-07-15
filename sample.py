from datetime import datetime
import pywhatkit
import threading
import time   
import keyboard as k

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen

kivy.require('2.0.0')  # Replace with your installed version if different

class MainScreen(BoxLayout):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.screen_manager = screen_manager

        button1 = Button(text="Image Sender")
        button1.bind(on_press=self.show_template1)
        self.add_widget(button1)

        button2 = Button(text="message sender")
        button2.bind(on_press=self.show_template2)
        self.add_widget(button2)

    def show_template1(self, instance):
        self.screen_manager.current = 'template1'

    def show_template2(self, instance):
        self.screen_manager.current = 'template2'

class Template1Screen(BoxLayout):
    def __init__(self, screen_manager,**kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.screen_manager = screen_manager
        
        self.num1_input = TextInput(hint_text="Enter phone number",  multiline=False)
        self.num2_input = TextInput(hint_text="Enter imagepath",  multiline=False)
        self.num3_input = TextInput(hint_text="Enter hours in 24format", multiline=False)
        self.num4_input = TextInput(hint_text="Enter minutes ",  multiline=False)
        self.num5_input = TextInput(hint_text="Enter caption ",  multiline=False)
        
        self.add_widget(self.num1_input)
        self.add_widget(self.num2_input)
        self.add_widget(self.num3_input)
        self.add_widget(self.num4_input)
        self.add_widget(self.num5_input)
        
        self.result_label = Label(text="Result will be displayed here")
        self.add_widget(self.result_label)
        
        add_button = Button(text="Add")
        add_button.bind(on_press=self.add_numbers)
        self.add_widget(add_button)
        
        # subtract_button = Button(text="Subtract")
        # subtract_button.bind(on_press=self.subtract_numbers)
        # self.add_widget(subtract_button)
    
    def add_numbers(self, instance):
        try:
            n = (self.num1_input.text)
            i = (self.num2_input.text)
            num3 = (self.num3_input.text)
            num4 = (self.num4_input.text)
            ca = (self.num5_input.text)
            t=(num3)+":"+(num4)
            now=datetime.now()
            c=now.strftime("%H:%M")
            while True:
                now=datetime.now()
                c=now.strftime("%H:%M")
                if t == c:
                    pywhatkit.sendwhats_image(n,i,ca)
                    print("sucessfully sent")
                    break
                else:
                    time.sleep(30)
                    now=datetime.now()
                    c=now.strftime("%H:%M")
                    print("waiting...")
            self.result_label.text = f"Success"
        except ValueError:
            self.result_label.text = "Please enter valid Details"

    def go_back(self, instance):
        self.screen_manager.current = 'main'

class Template2Screen(BoxLayout):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.screen_manager = screen_manager

        self.num1_input = TextInput(hint_text="Enter phone number", multiline=False)
        self.num2_input = TextInput(hint_text="Enter message", multiline=False)
        self.num3_input = TextInput(hint_text="Enter hours in 24format", input_filter='int', multiline=False)
        self.num4_input = TextInput(hint_text="Enter minutes ", input_filter='int', multiline=False)
        
        self.add_widget(self.num1_input)
        self.add_widget(self.num2_input)
        self.add_widget(self.num3_input)
        self.add_widget(self.num4_input)
        
        self.result_label = Label(text="Result will be displayed here")
        self.add_widget(self.result_label)
        
        add_button = Button(text="send")
        add_button.bind(on_press=self.add_numbers)
        self.add_widget(add_button)
        
        # subtract_button = Button(text="Subtract")
        # subtract_button.bind(on_press=self.subtract_numbers)
        # self.add_widget(subtract_button)
    
    def add_numbers(self, instance):
        try:
            num1 = (self.num1_input.text)
            num2 = (self.num2_input.text)
            num3 = int(self.num3_input.text)
            num4 = int(self.num4_input.text)
            pywhatkit.sendwhatmsg(num1,num2,num3,num4)
            k.on_press_key('enter')
            self.result_label.text = f"successfully sending"
        except ValueError:
            self.result_label.text = "Please enter valid numbers"

    def go_back(self, instance):
        self.screen_manager.current = 'main'

class TemplateApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        main_screen = Screen(name='main')
        main_screen.add_widget(MainScreen(screen_manager=self.screen_manager))
        self.screen_manager.add_widget(main_screen)

        template1_screen = Screen(name='template1')
        template1_screen.add_widget(Template1Screen(screen_manager=self.screen_manager))
        self.screen_manager.add_widget(template1_screen)

        template2_screen = Screen(name='template2')
        template2_screen.add_widget(Template2Screen(screen_manager=self.screen_manager))
        self.screen_manager.add_widget(template2_screen)

        return self.screen_manager

if __name__ == '__main__':
    TemplateApp().run()

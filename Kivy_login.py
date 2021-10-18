# from kivymd.app import MDApp
# from kivymd.uix.screen import Screen
# from kivymd.uix.textfield import MDTextField

# class SampleApp(MDApp):
#
#    def build(self):
#        screen = Screen()
#        username = MDTextField(text='Enter Username',
#                                pos_hint={'center_x': 0.5, 'center_y': 0.5},xxd
#                                size_hint_x=None,width=300)
#        screen.add_widget(username)
#        return screen
# SampleApp().run()

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder
from helpers import username_helper
from kivymd.uix.dialog import MDDialog

class AdenApp(MDApp):

    def build(self):
        screen = Screen()
        # To give color
        self.theme_cls.primary_palette = "Green"
        button = MDRectangleFlatButton(text='Login', pos_hint={'center_x': 0.5, 'center_y': 0.4},
                                        on_release=self.show_data)
        self.username = Builder.load_string(username_helper)
        screen.add_widget(self.username)
        screen.add_widget(button)
        return screen

    def show_data(self, obj):
        dialog = MDDialog(title= 'Username Check' ,text=self.username.text,
                        title_hint=(0.5, 1))
        dialog.open()

AdenApp().run()
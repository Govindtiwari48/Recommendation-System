# from kivy.core.text import Label
# from kivyauth.google_auth import initialize_google, login_google, logout_google
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from movie import recommend
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
# from kivy.uix.floatlayout import FloatLayout
# from kivy.utils import get_color_from_hex
# import numpy as np
# import pandas as pd
# from kivy.properties import ObjectProperty
# from oauthlib.oauth2 import WebApplicationClient
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp

KV = '''
ScreenManager:
    WelcomeScreen:
    MainScreen:
    SearchScreen:
    # ResultScreen:
    LoginScreen:

<WelcomeScreen>:
    name: 'welcome_screen'
    canvas:
        Color:
            rgba: 0, 0, 0, 1
        Rectangle:
            pos: self.pos
            size: self.size

    RelativeLayout:
        Image:
            source: "recommendation_logo.png"
            allow_stretch: True
            keep_ratio:False
            # size_hint: None, None
            # size: dp(200), dp(200)
            # pos_hint: {'center_x': 0.5, 'center_y': 0.6}

        MDRaisedButton:
            text:"Get Started"
            pos_hint: {'center_x': 0.5, 'center_y': 0.3}
            # halign:"center"
            # valign:"bottom"
            on_release: app.root.current = 'main_screen'

<MainScreen>:
    name: 'main_screen'
    canvas:
        Color:
            rgba: 0, 0, 0, 1
        Rectangle:
            pos: self.pos
            size: self.size

    FloatLayout:
        AnimatedImage:
            size_hint: None, None
            size: dp(800), dp(600)
            allow_stretch: True
            keep_ratio:False
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        MDFloatingActionButton:
            icon: "magnify"
            size_hint: None, None
            size: dp(56), dp(56)
            pos_hint: {'center_x': 0.5, 'center_y': 0.1}
            on_release: app.root.current = 'search_screen'

        # MDFloatingActionButton:
        #     icon: "home"
        #     size_hint: None, None
        #     size: dp(56), dp(56)
        #     pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        #     on_release: app.root.current = 'discover_screen'

        # MDFloatingActionButton:
        #     icon: "account"
        #     size_hint: None, None
        #     size: dp(56), dp(56)
        #     pos_hint: {'center_x': 0.7, 'center_y': 0.1}
        #     on_release: app.root.current = 'login_screen'

<SearchScreen>:
    name: 'search_screen'

    canvas:
        Color:
            rgba: 0, 0, 0, 1
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: "horizontal"
        MDTextField:
            id: search_input
            hint_text: "Enter your search query"
            multiline: False
            size_hint: None, None
            size: 800, 5
            pos_hint: {'center_x':0.5, 'center_y':0.95} 
        MDRectangleFlatButton:
            text: "Search"
            pos_hint: {'center_x':1, 'center_y':0.95}
            on_press: message_label.text(root.process_search() )
        Label:
            id: message_label
            text: ""
            size_hint_y: None
            height: self.texture_size[1]
    
    # FloatLayout:
    #     Label:
    #         id: output_label
    #         text: ""
    #         pos_hint: {'center_x': 0.5, 'center_y': 0.5}

    # RelativeLayout:
    #     Image:
    #         source: "search.png"
    #         allow_stretch: True
    #         keep_ratio:False
        # Label:
        #     text:"Write The First Letter In Capital"
        #     font_size: '32sp'
            
 
        # Label:
        #     id: recommendation_label
        #     text: ""
        #     size_hint: None, None
        #     size: 400, 50
        #     pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        #     
    FloatLayout:
        MDFloatingActionButton:
            icon: "arrow-left"
            size_hint: None, None
            size: dp(56), dp(56)
            pos_hint: {'center_x': 0.5, 'center_y': 0.1}
            on_release: app.root.current = 'main_screen'
    

# <ResultScreen>:
#     name: 'result_screen'
#     canvas:
#         Color:
#             rgba: 0, 0, 0, 1
#         Rectangle:
#             pos: self.pos
#             size: self.size
    
    

#     FloatLayout:
#         # Label:
#         #     text: "Home"
#         #     pos_hint: {'center_x': 0.5, 'center_y': 0.7}
#         #     font_size: '32sp'
# 
#         MDFloatingActionButton:
#             icon: "arrow-left"
#             size_hint: None, None
#             size: dp(56), dp(56)
#             pos_hint: {'center_x': 0.5, 'center_y': 0.3}
#             on_release: app.root.current = 'main_screen'
#             
# <LoginScreen>:
#     name: 'login_screen'
#     id: main_win
#     orientation: 'vertical'
#     spacing: 10
#     space_x: self.size[0]/3
#     canvas.before:
#         Color:
#             rgba: (1,1,1,1)
#         Rectangle:
#             size: self.size
#             pos:  self.pos
#     # Button:
#     #     text:"login with Google"
#     #     on_release:app.login()
#     BoxLayout:
#         size_hint_y: None
#         height:50
#         canvas.before:
#             Color:
#                 rgba: (.90,.20,.20,.90)
#             Rectangle:
#                 size: self.size
#                 pos:  self.pos
#         Label:
#             text: "Access Control"
#             bold: True
#             size_hint_x: .9
#     BoxLayout:
#         orientation: 'vertical'
#         padding: main_win.space_x, 10
#         spacing: 20
#         BoxLayout:
#             orientation: 'vertical'
#             spacing: 10
#             size_hint_y: .30
#             size_hint_x: 1
#             height: 100
#             Label:
#                 id: info
#                 text: " "
#                 markup: True
#                 size_hint_y: None
#                 height: 10
#             TextInput:
#                 id: username_field
#                 hint_text: "User Name"
#                 multiline: False
#                 focus: True
#                 # on_text_validate: pwd_field.focus= True
#             TextInput:
#                 id: pwd_field
#                 hint_text: "Password"
#                 multiline: False
#                 password: True
#                 # on_text_validate: root.validate_user()
#         Label:
#             id: sp
#             size_hint_y: None
#             height: 10
#         Button:
#             text: "Sign In"
#             size_hint_y: .2
#             size_hint_x: .90
#             height: 20
#             background_color: (.90, .20, .20,.90)
#             background_normal: ''
#             on_release: root.validate_user()
#         Label:
#             id: sp2

# <LoginScreen>:
#     name: 'login_screen'
#     canvas:
#         Color:
#             rgba: 0, 0, 0, 1
#         Rectangle:
#             pos: self.pos
#             size: self.size
# 
#     FloatLayout:
#         Label:
#             text: "Login Screen"
#             pos_hint: {'center_x': 0.5, 'center_y': 0.7}
#             font_size: '32sp'
# 
#         MDFloatingActionButton:
#             icon: "arrow-left"
#             size_hint: None, None
#             size: dp(56), dp(56)
#             pos_hint: {'center_x': 0.5, 'center_y': 0.3}
#             on_release: app.root.current = 'main_screen'
# '''


class WelcomeScreen(Screen):
    pass


class MainScreen(Screen):
    pass


class AnimatedImage(Image):
    def __init__(self, **kwargs):
        super(AnimatedImage, self).__init__(**kwargs)
        self.frames = []
        self.index = 0
        self.load_frames()
        self.anim_delay = 3  # Delay between each frame (adjust as needed)
        self.texture = self.frames[0].texture
        Clock.schedule_interval(self.update_frame, self.anim_delay)

    def load_frames(self):
        image_filenames = ['avatar.png', 'batman.png', 'conjuring.png', 'avengerendgame.png', 'aquaman.png',
                           'mission.png', 'spiderman.png']
        for filename in image_filenames:
            image = Image(source=filename)
            self.frames.append(image)

    def update_frame(self, df):
        self.index = (self.index + 1) % len(self.frames)
        self.texture = self.frames[self.index].texture


class SearchScreen(Screen):
    def process_search(self):
        search_query = self.ids.search_input.text
        recommendations = recommend(search_query)
        self.pri = Button(text=recommendations,border=(30,30,30,30,), size_hint=(0.3,0.3),pos_hint={"x":.35,"y":.3})
        self.ids.search_input.add_widget(self.pri)

        # self.display_recommendations(recommendations)












class DiscoverScreen(Screen):
    pass


class LoginScreen(Screen):
    pass
    # def build(self):
    #     client_id = open("client_id.txt").read()
    #     client_secret = open("client_secret.txt").read()
    #     initialize_google(self.after_login, self.error_listener, client_id, client_secret)
    #     return Builder.load_string(KV)
    #
    # def after_login(self):
    #     # Handle the user's successful login here
    #     pass
    #
    # def error_listener(self, error):
    #     # Handle any error that occurs during login
    #     print(f"Login error: {error}")


class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        sm = Builder.load_string(KV)
        return sm

    # def login(self):
    #     login_google(self.after_login, self.error_listener)
    #
    # def after_login(self):
    #     # Handle the user's successful login here
    #     pass
    #
    # def error_listener(self, error):
    #     # Handle any error that occurs during login
    #     print(f"Login error: {error}")
    #


if __name__ == '__main__':
    MyApp().run()

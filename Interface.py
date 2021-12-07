from typing import Text
import kivymd
import Load_Sentiment as sentiment
import Twitter_API as api
from IPython import get_ipython
from kivymd.app import MDApp
from kivymd.uix.label import Label
from kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.textinput import TextInput
from kivymd.uix.textfield import MDTextField
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivy.properties import ObjectProperty, StringProperty

#create a grid using the grid layout class from kivy        
class MyGrid(MDGridLayout):
    tweet = ObjectProperty(None)
    

    #pressed method, when a button is pressed get the name value and print it too the console
    def pressed(self):
        text = self.tweet.text
        prediction = sentiment.predict(text)

        self.ids.tweet_sentiment.text = f'{prediction} sentiment'

        #print name to screen
        print("Tweet:", text, " Sentiment: ", prediction)

        #post status to twitter
        #api.postStatus(text)  

        #reset name to plank
        self.tweet.text = ""  

           

#class for Main app
class MainApp(MDApp):
    #build the app

    def build(self):
        screen = Screen()
        screen.add_widget(MyGrid())
        return screen

MainApp().run()
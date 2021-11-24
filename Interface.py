import kivy
import Load_Sentiment as sentiment
from IPython import get_ipython
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

#create a grid using the grid layout class from kivy        
class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

        #decide on number of coloumns to use for main layout    
        self.cols = 1

        #create a grid layout inside the current one
        self.inside = GridLayout() 
        self.inside.cols = 2

        #region InsideLayout

        #create a label, then a text box and add it too the grid
        self.inside.add_widget(Label(text="Tweet: "))
        self.tweet = TextInput(multiline=False)
        self.inside.add_widget(self.tweet)

        #endregion InsideLayout

        #add the layout described above to main layout
        self.add_widget(self.inside)

        #create a button and add it to grid
        self.submit = Button(text="Submit", font_size=40)  
        self.add_widget(self.submit)

        #we want to run the pressed method on the submit button
        self.submit.bind(on_press=self.pressed)

    #pressed method, when a button is pressed get the name value and print it too the console
    def pressed(self, instance):
        #get the name
        tweet = self.tweet.text

        prediction = sentiment.predict(tweet)

        #print name to screen
        print("Tweet:", tweet, " Sentiment: ", prediction)

        #reset name to plank
        self.tweet.text = ""       

#class for Main app
class MainApp(App):
    #build the app
    def build(self):
        return MyGrid()


#used to run the app we just built
if __name__ == '__main__':
    app = MainApp()
    app.run()
import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
class MyGrid(GridLayout):
    def __init__(self,**kwargs):
        super(MyGrid,self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="name"))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)
        
        self.add_widget(Label(text="roll"))
        self.roll = TextInput(multiline=False)
        self.add_widget(self.roll)


        self.submit = Button(text="submit")
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)


    def pressed(self,instance):
        name = self.name.text
        roll = self.roll.text
        con = "Your Name: "+name+" Roll: "+roll
        print(name,":",roll,con)
        c = Label(text=con)
        popup = Popup(title='Alert message',content=c,size_hint=(None, None), size=(400, 400),auto_dismiss=True)
        popup.open()       
       # popup.dismiss()

     
class MyApp(App):
    def build(self):
        return MyGrid()

if __name__== "__main__":
    MyApp().run()




#https://itsfoss.com/could-not-get-lock-error/

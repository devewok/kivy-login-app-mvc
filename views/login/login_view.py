from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file("views/login/login_design.kv")
class LoginView(Screen):

    status=ObjectProperty()
    username=ObjectProperty()
    password=ObjectProperty()
    password2=ObjectProperty()
    login_btn=ObjectProperty()

    def set_status(self,color,text):
        self.status.color=color
        self.status.text=text

    def get_data(self):
        return self.username.text,self.password.text,self.password2.text


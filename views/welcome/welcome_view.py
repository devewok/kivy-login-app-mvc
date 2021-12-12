from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

Builder.load_file("views/welcome/welcome_design.kv")
class WelcomeView(Screen):

    greating=ObjectProperty()
    def __init__(self,user,**kw):
        super().__init__(**kw)
        self.user=user

    def on_pre_enter(self, *args):
        self.greating.text+=self.user.username




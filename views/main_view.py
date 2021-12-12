from kivy.app import App
from kivy.config import Config
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager
from views.login.login_view import LoginView
from views.welcome.welcome_view import WelcomeView

Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '500')
Config.write()

Builder.load_file("views/main_design.kv")
class WindowManager(ScreenManager):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class LoginApp(App):

    def __init__(self,user,**kwargs):
        super().__init__(**kwargs)
        self.user=user
        self.sm=WindowManager()
        self.login_view=LoginView(name="login")
        self.welcome_view=WelcomeView(name="welcome",user=self.user)

    def switch_to_welcome(self):
        self.sm.switch_to(self.welcome_view)

    def build(self):
        self.title="Login"
        self.sm.add_widget(self.login_view)
        self.sm.add_widget(self.welcome_view)
        return self.sm

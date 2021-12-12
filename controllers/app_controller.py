from controllers.login_controller import LoginController

class AppController():


    def __init__(self,app,user) -> None:
        self.app=app
        self.user=user
        self.login_controller=LoginController(app)
        self.app.login_view.login_btn.fbind("on_press",self.on_login)

    def on_login(self, *args):
        username,password,password2=self.app.login_view.get_data()
        result=self.login_controller.login(username,password,password2)
        if result:
            self.user.set_user(username,password)
            self.app.switch_to_welcome()
        else:
            self.app.login_view.set_status((1,0,0,1),"Something is wrong")



    def start(self)->None:
        self.app.run()


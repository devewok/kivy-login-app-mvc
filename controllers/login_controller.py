
class LoginController():


    def __init__(self,app) -> None:
        self.app=app
        self.username="foo"
        self.password="bar"

    def login(self,username,password,password2):
        self.app.login_view.set_status((0,1,0,1),"Validating..")
        if password2!=password:
            return False
        if self.password!=password:
            return False
        if self.username!=username:
            return False
        return True



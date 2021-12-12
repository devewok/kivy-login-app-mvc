from controllers.app_controller import AppController
from views.main_view import LoginApp
from models.user import User

if __name__=="__main__":
    user=User()
    app=LoginApp(user)
    controller=AppController(app,user)
    controller.start()

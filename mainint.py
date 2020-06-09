import PyQt5, json
from PyQt5 import QtWidgets
from uiFiles import mainWin
from vkscript import authct

mainVk = None

class mainWind(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainWind, self).__init__()
        self.ui = mainWin.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.startButton.clicked.connect(self.start)
        self.initUser()
        self.userScreen(self)
        
    def initUser(self):
        f = open('vkscript/settings.json','r')
        userFromSettings = json.load(f)
        number = userFromSettings['number']
        password = userFromSettings['password']
        user = (number,password)
        vk = authct.auth(user,self)
        mainVk = vk
        
    def userScreen(self):
        thisUser = mainVk.users.get()
        name = thisUser[0]['first_name']
        surname = thisUser[0]['last_name']
        self.greetingsLabel.setText("Приветствую тебя, {name} {surname}".format(name=name,surname=surname))
        
    def start(self):
        pass
        
    

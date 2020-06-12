import PyQt5, json
from vkscript import authct
from PyQt5 import QtWidgets
from uiFiles import authUI

class authint(QtWidgets.QMainWindow):
    def __init__(self):
        super(authint, self).__init__()
        self.ui = authUI.Ui_MainWindow(); 
        self.ui.setupUi(self)
        self.ui.startButton.clicked.connect(self.storeValues)
        self.show()
        
    def storeValues(self):
        login = self.ui.loginLine.text()
        try:
            int(login)
        except ValueError:
            QtWidgets.QMessageBox.question(self, "ошибка","в поле номера введены не только цифры. Повторите попытку",QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
            return
        
        password = self.ui.passLine.text()
        user = (login,password)
        result = authct.auth(user, self)
        if result == 1:
            return
        
        print(result)
        f = open('settings.json','w')
        userDict = {"number":login,"password":password}
        json.dump(userDict, f)
        f.close()
        self.close()
        

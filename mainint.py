import PyQt5, json, os
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QThread
from uiFiles import mainWin
from vkscript import authct, working

percentOfVl = "процент выполнения: "

class mainWind(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainWind, self).__init__()
        self.ui = mainWin.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.startButton.clicked.connect(self.mainCycle)
        self.ui.aboutProgButton.clicked.connect(self.about)
        self.ui.outlogButton.clicked.connect(self.outlog)
        self.initUser()
        self.userScreen()
        self.show()
        
    def initUser(self):
        f = open('settings.json','r')
        userFromSettings = json.load(f)
        number = userFromSettings['number']
        password = userFromSettings['password']
        user = (number,password)
        self.vk = authct.auth(user,self)
        
    def userScreen(self):
        thisUser = self.vk.users.get()
        name = thisUser[0]['first_name']
        surname = thisUser[0]['last_name']
        self.ui.greetingsLabel.setText("Приветствую тебя, {name} {surname}".format(name=name,surname=surname))
    
    def mainCycle(self):
        self.ui.progressBarLabel.setText(percentOfVl + "получение основной информации...")
        self.ui.chooseCountSpinBox.setEnabled(False)
        self.ui.startButton.setEnabled(False)
        self.ui.aboutProgButton.setEnabled(False)
        self.ui.outlogButton.setEnabled(False)
        self.howMPhots = 0
        self.fullyAmmountOfPhotos = self.ui.chooseCountSpinBox.value() / 100
        self.countOfCycles = int(self.ui.chooseCountSpinBox.value() / 50)
        self.remainderC = self.ui.chooseCountSpinBox.value() % 50
        if (self.remainderC > 0) or (self.remainderC < 0) or (self.countOfCycles == 0):
            self.ui.chooseCountSpinBox.setEnabled(True)
            self.ui.startButton.setEnabled(True)
            self.ui.progressBarLabel.setText(percentOfVl + "ошибка: вы выбрали не то число...")
            return
            
        self.albumCreate()
        
        for i in range(self.countOfCycles):
            self.getPhotos()
            self.photoMove()
        
        self.ui.chooseCountSpinBox.setEnabled(True)
        self.ui.startButton.setEnabled(True)
        self.ui.aboutProgButton.setEnabled(True)
        self.ui.outlogButton.setEnabled(True)
        self.ui.progressBarLabel.setText(percentOfVl + "готово...")  
            
    def photoMove(self):
        self.phmv = working.movePhoto(win=self,vk=self.vk,phids=self.photosList,albid=self.albumNeeded,parent=self)
        self.phmv.start()
        while self.phmv.isFinished() == False:
            pass
            
        self.phmv.exit()
        
    def albumCreate(self):
        self.albumNeeded = 0
        self.titleOfAlbum = "SavedPhotos"
        self.allAlbums = self.vk.photos.getAlbums()
        self.allAlbums = self.allAlbums['items']
        for i in self.allAlbums:
            if i['title'] == self.titleOfAlbum:
                self.albumNeeded = i['id']
                print(i['title'])
                break
        if self.albumNeeded == "":
            self.vk.photos.createAlbum(title=self.titleOfAlbum)
        
        
    def getPhotos(self):
        self.photosList = list()
        allPhotos = self.vk.photos.get(album_id="saved")
        for i in allPhotos['items']:
            self.photosList.append(i['id'])
            
        
     
    def about(self):
        pass
    
    def outlog(self):
        os.remove('settings.json')
        QtWidgets.QMessageBox.question(self, "Разлогинились","разлогинились успешно",QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        self.close()

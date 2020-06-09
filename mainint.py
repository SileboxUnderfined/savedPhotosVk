import PyQt5, json
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
        self.ui.startButton.clicked.connect(self.start)
        self.ui.aboutProgButton.clicked.connect(self.about)
        self.initUser()
        self.userScreen()
        self.show()
        
    def initUser(self):
        f = open('vkscript/settings.json','r')
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
        
    def start(self):
        self.ui.progressBarLabel.setText(percentOfVl + "получение основной информации...")
        

        
        self.mncl = mainCycle(vk=self.vk,win=self)
        self.mncl.start()
        self.mncl.wait()
        

        
        self.ui.progressBarLabel.setText(percentOfVl + "готово...")

    
    """def mainCycle(self):
        self.albumCreate()
        self.howMPhots = 0
        self.fullyAmmountOfPhotos = self.ui.chooseCountSpinBox.value() / 100
        self.countOfCycles = int(self.ui.chooseCountSpinBox.value() / 50)
        for i in range(self.countOfCycles):
            self.getPhotos()
            self.photoMove()"""
            
    def photoMove(self):
        self.phmv = working.movePhoto(win=self,vk=self.vk,phids=self.photosList,albid=self.albumNeeded,parent=self)
        self.phmv.start()
        
        
    
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
        

class mainCycle(QThread):
    def __init__(self,vk,win):
        super().__init__()
        self.titleOfAlbum = "SavedPhotos"
        self.vk = vk
        self.win = win
        self.win.ui.chooseCountSpinBox.setEnabled(False)
        self.win.ui.startButton.setEnabled(False)
        
    def run(self):
        self.albumCreate()
        self.howMPhots = 0
        self.fullyAmmountOfPhotos = self.win.ui.chooseCountSpinBox.value() / 100
        self.countOfCycles = int(self.win.ui.chooseCountSpinBox.value() / 50)
        for i in range(self.countOfCycles):
            self.getPhotos()
            self.photoMove()
        
        self.win.ui.chooseCountSpinBox.setEnabled(True)
        self.win.ui.startButton.setEnabled(True)
    
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
    
    def photoMove(self):
        self.phmv = working.movePhoto(win=self,vk=self.vk,phids=self.photosList,albid=self.albumNeeded,parent=self)
        self.phmv.start()

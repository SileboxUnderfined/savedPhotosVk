import PyQt5, vk_api
from PyQt5.QtCore import QThread

class movePhoto(QThread):
    def __init__(self, win, vk, phids,albid, parent=None):
        super().__init__()
        self.mainwindow = win
        self.vk = vk
        self.phids = phids
        self.albid = albid
        print(self.albid)
        
    def run(self):
        for i in range(len(self.phids)):
            self.mainwindow.win.ui.progressBarLabel.setText("Перемещение фотографии с id = " + str(self.phids[i]))
            self.vk.photos.move(photo_id=self.phids[i], target_album_id=self.albid)


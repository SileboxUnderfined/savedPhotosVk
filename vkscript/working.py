import PyQt5, vk_api
from PyQt5.QtCore import QThread

percentOfVl = "процент выполнения: "

class movePhoto(QThread):
    def __init__(self, win, vk, phids,albid, parent=None):
        super().__init__()
        self.mainwindow = win
        self.vk = vk
        self.phids = phids
        self.albid = albid
        print(self.albid)
        
    def run(self):
        self.mainwindow.ui.progressBar.setMaximum(len(self.phids))
        self.mainwindow.ui.progressBar.setValue(0)
        for i in range(len(self.phids)):
            self.mainwindow.ui.progressBarLabel.setText("Перемещение фотографии с id = " + str(self.phids[i]))
            self.vk.photos.move(photo_id=self.phids[i], target_album_id=self.albid)
            self.mainwindow.ui.progressBar.setValue(self.mainwindow.ui.progressBar.value() + 1)
        
        self.mainwindow.ui.chooseCountSpinBox.setEnabled(True)
        self.mainwindow.ui.startButton.setEnabled(True)
        self.mainwindow.ui.progressBarLabel.setText(percentOfVl + "готово...")

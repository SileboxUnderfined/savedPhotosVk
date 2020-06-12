import PyQt5
from PyQt5 import QtWidgets
import authint, mainint
import sys, os

def main():
    app = QtWidgets.QApplication([])
    app.setStyle("Fusion")
    application = None
    if os.path.isfile("settings.json") == False:
        application = authint.authint()
        app.exec()
        
    application = mainint.mainWind()
    sys.exit(app.exec())
        
if __name__ == "__main__":
    main()


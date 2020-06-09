import PyQt5
from PyQt5 import QtWidgets
import authint, mainint
import sys, os

def main():
    app = QtWidgets.QApplication([])
    application = None
    if os.path.isfile("vkscript/settings.json") == False:
        application = authint.authint()
        app.exec()
        
    application = mainint.mainWind()
    sys.exit(app.exec())
        
if __name__ == "__main__":
    main()


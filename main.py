import PyQt5
from PyQt5 import QtWidgets
import mainint
import sys, os



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = None
    if os.path.isfile('vkscript/settings.json') == False:
        application = authint.authint()
        application.show()
        application = mainint.mainWind()
        application.show()
  
    sys.exit(app.exec())


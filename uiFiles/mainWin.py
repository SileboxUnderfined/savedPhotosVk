# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWin.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(272, 453)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.greetingsLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.greetingsLabel.sizePolicy().hasHeightForWidth())
        self.greetingsLabel.setSizePolicy(sizePolicy)
        self.greetingsLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.greetingsLabel.setObjectName("greetingsLabel")
        self.horizontalLayout.addWidget(self.greetingsLabel)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.chooseCountLabel = QtWidgets.QLabel(self.centralwidget)
        self.chooseCountLabel.setObjectName("chooseCountLabel")
        self.verticalLayout.addWidget(self.chooseCountLabel)
        self.chooseCountSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.chooseCountSpinBox.setMaximum(10000)
        self.chooseCountSpinBox.setSingleStep(50)
        self.chooseCountSpinBox.setObjectName("chooseCountSpinBox")
        self.verticalLayout.addWidget(self.chooseCountSpinBox)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.progressBarLabel = QtWidgets.QLabel(self.centralwidget)
        self.progressBarLabel.setObjectName("progressBarLabel")
        self.verticalLayout_2.addWidget(self.progressBarLabel)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setStyleSheet("height: 1;")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setObjectName("startButton")
        self.verticalLayout_3.addWidget(self.startButton)
        self.aboutProgButton = QtWidgets.QPushButton(self.centralwidget)
        self.aboutProgButton.setObjectName("aboutProgButton")
        self.verticalLayout_3.addWidget(self.aboutProgButton)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 272, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Работа со сохранёнными фотографиями вк"))
        self.greetingsLabel.setText(_translate("MainWindow", "label"))
        self.chooseCountLabel.setText(_translate("MainWindow", "выберите количество фотографий"))
        self.progressBarLabel.setText(_translate("MainWindow", "Процент выполнения:"))
        self.startButton.setText(_translate("MainWindow", "Начать"))
        self.aboutProgButton.setText(_translate("MainWindow", "о программе"))

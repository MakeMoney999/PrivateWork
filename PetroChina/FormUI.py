# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FormUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Loadform2_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.Loadform2_pushButton.setGeometry(QtCore.QRect(20, 240, 93, 28))
        self.Loadform2_pushButton.setObjectName("Loadform2_pushButton")
        self.Loadform1_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.Loadform1_pushButton.setGeometry(QtCore.QRect(20, 310, 93, 28))
        self.Loadform1_pushButton.setObjectName("Loadform1_pushButton")
        self.InfoShow_plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.InfoShow_plainTextEdit.setGeometry(QtCore.QRect(400, 10, 391, 531))
        self.InfoShow_plainTextEdit.setObjectName("InfoShow_plainTextEdit")
        self.Analyst_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.Analyst_pushButton.setGeometry(QtCore.QRect(20, 370, 93, 28))
        self.Analyst_pushButton.setObjectName("Analyst_pushButton")
        self.Loadform2_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.Loadform2_lineEdit.setGeometry(QtCore.QRect(20, 270, 371, 21))
        self.Loadform2_lineEdit.setObjectName("Loadform2_lineEdit")
        self.Loadform1_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.Loadform1_lineEdit.setGeometry(QtCore.QRect(20, 340, 371, 21))
        self.Loadform1_lineEdit.setObjectName("Loadform1_lineEdit")
        self.Saveform_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.Saveform_pushButton.setGeometry(QtCore.QRect(20, 400, 93, 28))
        self.Saveform_pushButton.setObjectName("Saveform_pushButton")
        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(100, 70, 200, 98))
        self.Logo.setText("")
        self.Logo.setObjectName("Logo")
        self.SheetName2 = QtWidgets.QLabel(self.centralwidget)
        self.SheetName2.setGeometry(QtCore.QRect(140, 240, 251, 28))
        self.SheetName2.setText("")
        self.SheetName2.setObjectName("SheetName2")
        self.SheetName1 = QtWidgets.QLabel(self.centralwidget)
        self.SheetName1.setGeometry(QtCore.QRect(140, 310, 251, 28))
        self.SheetName1.setText("")
        self.SheetName1.setObjectName("SheetName1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Loadform2_pushButton.setText(_translate("MainWindow", "???????????????"))
        self.Loadform1_pushButton.setText(_translate("MainWindow", "???????????????"))
        self.Analyst_pushButton.setText(_translate("MainWindow", "??????"))
        self.Saveform_pushButton.setText(_translate("MainWindow", "????????????"))

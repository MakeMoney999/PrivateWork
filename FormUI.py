# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FormUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 70, 335, 98))
        self.label.setText("")
        self.label.setObjectName("label")
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
        self.Loadform2_pushButton.setText(_translate("MainWindow", "加载库存表"))
        self.Loadform1_pushButton.setText(_translate("MainWindow", "加载采购表"))
        self.Analyst_pushButton.setText(_translate("MainWindow", "分析"))
        self.Saveform_pushButton.setText(_translate("MainWindow", "保存结果"))

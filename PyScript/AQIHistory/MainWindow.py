# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(593, 510)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 51, 21))
        self.label.setObjectName("label")
        self.lineEdit_city = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_city.setGeometry(QtCore.QRect(70, 10, 161, 21))
        self.lineEdit_city.setObjectName("lineEdit_city")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 10, 71, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit_code = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_code.setGeometry(QtCore.QRect(400, 10, 161, 21))
        self.lineEdit_code.setObjectName("lineEdit_code")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 61, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(320, 50, 61, 21))
        self.label_4.setObjectName("label_4")
        self.dateEdit_start = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_start.setGeometry(QtCore.QRect(90, 50, 110, 24))
        self.dateEdit_start.setObjectName("dateEdit_start")
        self.dateEdit_end = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_end.setGeometry(QtCore.QRect(400, 50, 110, 24))
        self.dateEdit_end.setObjectName("dateEdit_end")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 130, 551, 321))
        self.listWidget.setObjectName("listWidget")
        self.pushButton_active = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_active.setGeometry(QtCore.QRect(440, 90, 113, 32))
        self.pushButton_active.setObjectName("pushButton_active")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 593, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionxs = QtWidgets.QAction(MainWindow)
        self.actionxs.setObjectName("actionxs")
        self.menuFile.addAction(self.actionxs)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "获取城市小时数据"))
        self.label.setText(_translate("MainWindow", "城市:"))
        self.label_2.setText(_translate("MainWindow", "气象点编码:"))
        self.label_3.setText(_translate("MainWindow", "开始日期:"))
        self.label_4.setText(_translate("MainWindow", "截止日期:"))
        self.pushButton_active.setText(_translate("MainWindow", "开始"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionxs.setText(_translate("MainWindow", "存储路径"))

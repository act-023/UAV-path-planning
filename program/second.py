# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'second.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 488)
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(60, 50, 131, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(MainWindow)
        self.label_2.setGeometry(QtCore.QRect(60, 100, 131, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(MainWindow)
        self.label_3.setGeometry(QtCore.QRect(50, 150, 131, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(MainWindow)
        self.label_4.setGeometry(QtCore.QRect(50, 200, 131, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(MainWindow)
        self.label_5.setGeometry(QtCore.QRect(50, 250, 131, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(MainWindow)
        self.label_6.setGeometry(QtCore.QRect(80, 310, 101, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(MainWindow)
        self.label_7.setGeometry(QtCore.QRect(50, 360, 131, 16))
        self.label_7.setObjectName("label_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(MainWindow)
        self.lineEdit_8.setGeometry(QtCore.QRect(230, 50, 141, 21))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(MainWindow)
        self.lineEdit_9.setGeometry(QtCore.QRect(230, 100, 141, 21))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(MainWindow)
        self.lineEdit_10.setGeometry(QtCore.QRect(230, 150, 141, 21))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(MainWindow)
        self.lineEdit_11.setGeometry(QtCore.QRect(230, 200, 141, 21))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(MainWindow)
        self.lineEdit_12.setGeometry(QtCore.QRect(230, 250, 141, 21))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(MainWindow)
        self.lineEdit_13.setGeometry(QtCore.QRect(230, 310, 141, 21))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(MainWindow)
        self.lineEdit_14.setGeometry(QtCore.QRect(230, 360, 141, 21))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.pushButton_2 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 430, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(520, 430, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "无人机设置"))
        self.label.setText(_translate("MainWindow", "最大转弯角(°)："))
        self.label_2.setText(_translate("MainWindow", "最大爬升角(°)："))
        self.label_3.setText(_translate("MainWindow", "最小飞行距离(m)："))
        self.label_4.setText(_translate("MainWindow", "最小飞行高度(m)："))
        self.label_5.setText(_translate("MainWindow", "最大飞行高度(m)："))
        self.label_6.setText(_translate("MainWindow", "威胁系数(l)："))
        self.label_7.setText(_translate("MainWindow", "飞行时间限制(s)："))
        self.pushButton_2.setText(_translate("MainWindow", "重置"))
        self.pushButton.setText(_translate("MainWindow", "确定"))

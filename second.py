# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'second.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class child1(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 488)
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(60, 30, 131, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(MainWindow)
        self.label_2.setGeometry(QtCore.QRect(60, 80, 131, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(MainWindow)
        self.label_3.setGeometry(QtCore.QRect(50, 130, 131, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(MainWindow)
        self.label_4.setGeometry(QtCore.QRect(50, 180, 131, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(MainWindow)
        self.label_5.setGeometry(QtCore.QRect(50, 230, 131, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(MainWindow)
        self.label_6.setGeometry(QtCore.QRect(80, 290, 101, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(MainWindow)
        self.label_7.setGeometry(QtCore.QRect(50, 340, 131, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(MainWindow)
        self.label_8.setGeometry(QtCore.QRect(50, 390, 131, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(MainWindow)
        self.label_9.setGeometry(QtCore.QRect(30, 440, 151, 16))
        self.label_9.setObjectName("label_9")
        self.lineEdit_8 = QtWidgets.QLineEdit(MainWindow)
        self.lineEdit_8.setGeometry(QtCore.QRect(230, 30, 141, 21))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(MainWindow)
        self.lineEdit_9.setGeometry(QtCore.QRect(230, 80, 141, 21))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(MainWindow)
        self.lineEdit_10.setGeometry(QtCore.QRect(230, 130, 141, 21))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(MainWindow)
        self.lineEdit_11.setGeometry(QtCore.QRect(230, 180, 141, 21))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(MainWindow)
        self.lineEdit_12.setGeometry(QtCore.QRect(230, 230, 141, 21))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(MainWindow)
        self.lineEdit_13.setGeometry(QtCore.QRect(230, 290, 141, 21))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(MainWindow)
        self.lineEdit_14.setGeometry(QtCore.QRect(230, 340, 141, 21))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_15 = QtWidgets.QLineEdit(MainWindow)
        self.lineEdit_15.setGeometry(QtCore.QRect(230, 390, 141, 21))
        self.lineEdit_15.setObjectName("lineEdit_14")
        self.lineEdit_16 = QtWidgets.QLineEdit(MainWindow)
        self.lineEdit_16.setGeometry(QtCore.QRect(230, 440, 141, 21))
        self.lineEdit_16.setObjectName("lineEdit_14")
        self.pushButton = QtWidgets.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(520, 440, 93, 28))
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
        self.label_8.setText(_translate("MainWindow", "无人机电量（%）："))
        self.label_9.setText(_translate("MainWindow", "单位距离能耗(W·h)："))
        self.pushButton.setText(_translate("MainWindow", "OK"))






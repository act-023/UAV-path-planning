# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from UAV import *
from env import *
from env import Env
from  watch_uav import *
from PyQt5.QtGui import QPixmap
from building import *
from third import child2
from PyQt5.QtWidgets import QDialog, QLineEdit, QVBoxLayout, QPushButton, QInputDialog, QLabel, QFileDialog, QTableWidget, QTableWidgetItem, QMessageBox
import pandas as pd
from PyQt5.QtCore import Qt
import numpy


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(829, 632)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(-60, -60, 951, 721))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("blue_label.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(62, 150, 711, 391))
        self.label.setText("")
        pixmap = QPixmap("p1.jpg")
        # 调整图片大小以适应标签大小
        #pixmap = pixmap.scaledToWidth(300)
        # 显示图片
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 0, 731, 200))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.pushButton_1 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_1.clicked.connect(self.function1)
        self.pushButton_1.setStyleSheet("QPushButton {\n"
"                      font-size: 16px;\n"
"                      padding: 15px;\n"
"                      border-radius: 5px;\n"
"                      background-color: #4CAF50;\n"
"                      color: white;\n"
"                      }\n"
"                      QPushButton:hover {\n"
"                      background-color: #45a049;\n"
"                      }")
        self.pushButton_1.setObjectName("pushButton_1")
        self.horizontalLayout.addWidget(self.pushButton_1)

        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        #self.pushButton.clicked.connect(self.function1)
        self.pushButton.setStyleSheet("QPushButton {\n"
"                      font-size: 16px;\n"
"                      padding: 15px;\n"
"                      border-radius: 5px;\n"
"                      background-color: #4CAF50;\n"
"                      color: white;\n"
"                      }\n"
"                      QPushButton:hover {\n"
"                      background-color: #45a049;\n"
"                      }")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.clicked.connect(self.input)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"                      font-size: 16px;\n"
"                      padding: 15px;\n"
"                      border-radius: 5px;\n"
"                      background-color: #4CAF50;\n"
"                      color: white;\n"
"                      }\n"
"                      QPushButton:hover {\n"
"                      background-color: #45a049;\n"
"                      }")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.clicked.connect(self.function3)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"                      font-size: 16px;\n"
"                      padding: 15px;\n"
"                      border-radius: 5px;\n"
"                      background-color: #4CAF50;\n"
"                      color: white;\n"
"                      }\n"
"                      QPushButton:hover {\n"
"                      background-color: #45a049;\n"
"                      }")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)


        self.retranslateUi(Form)
        self.inputs = []
        self.inputs2 = []
        self.temp = []
        self.is_use = 1
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "无人机航迹规划系统"))
        self.pushButton.setText(_translate("Form", "无人机配置"))
        self.pushButton_1.setText(_translate("Form", "环境配置"))
        self.pushButton_2.setText(_translate("Form", "任务点设置"))
        self.pushButton_3.setText(_translate("Form", "航迹规划"))

    def function2(self):
        n_states = 10  # 状态空间的数量
        n_actions = 5  # 动作集的数量
        LEARNING_RATE = 0.001  # 学习率

        # 创建环境实例
        env = Env(n_states, n_actions, LEARNING_RATE)

        env.reset()
        env.render()
        plt.savefig("function1.jpg")
        # 加载图片
        pixmap = QPixmap("function1.jpg")
        # 调整图片大小以适应标签大小
        pixmap = pixmap.scaledToWidth(300)
        # 显示图片
        self.label.setPixmap(pixmap)
        # 自适应大小
        self.label.setScaledContents(True)


    def input(self):
        # 创建并显示输入对话框
        #app = QApplication(sys.argv)
        dialog = InputDialog_2()

        if dialog.exec_() == dialog.Accepted:
            print('输入框1:', dialog.get_inputs()[0])
            print('输入框2:', dialog.get_inputs()[1])
            print('输入框1:', dialog.get_inputs()[2])
            print('输入框2:', dialog.get_inputs()[3])
            print('输入框1:', dialog.get_inputs()[4])
            print('输入框2:', dialog.get_inputs()[5])

            #print(dialog.get_inputs())
            try:
                value = float(dialog.lineEdit_3.text())
                if not (13 <= value <= 17):  # 假设我们检查是否在10到100之间
                    dialog.setFocus()
                    QMessageBox.warning(dialog, 'Error', '与建筑物重合，请重新输入')
                    # dialog.lineEdit_3.clear()  # 清空输入以便重新输入

            except ValueError:
                # QMessageBox.warning(self, 'Error', 'Value must be between 10 and 100')
                dialog.lineEdit_3.clear()  # 清空输入以便重新输入

            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.scatter(int(dialog.get_inputs()[0]), int(dialog.get_inputs()[1]), int(dialog.get_inputs()[2]), c='red')
            ax.scatter(int(dialog.get_inputs()[3]), int(dialog.get_inputs()[4]), int(dialog.get_inputs()[5]), c='blue')
            # fig.show()

            plt.savefig("function1.jpg")
            pixmap = QPixmap("function1.jpg")
            self.label.setPixmap(pixmap)


            # ax = fig.add_subplot(111, projection='3d')
            # ax.scatter(int(dialog.get_inputs()[0]), int(dialog.get_inputs()[1]), int(dialog.get_inputs()[2]), c='red')
            # ax.scatter(int(dialog.get_inputs()[3]), int(dialog.get_inputs()[4]), int(dialog.get_inputs()[5]), c='blue')
            # # fig.show()
            # plt.savefig("function1.jpg")
            # pixmap = QPixmap("function1.jpg")
            # self.label.setPixmap(pixmap)
        #sys.exit(app.exec_())

    def function1(self):
        len = 100
        width = 100
        h = 22
        map = np.zeros((len, width, h))
        bds = []

        class building():
            def __init__(self, x, y, l, w, h):
                self.x = x  # 建筑中心x坐标
                self.y = y  # 建筑中心y坐标
                self.l = l  # 建筑长半值
                self.w = w  # 建筑宽半值
                self.h = h  # 建筑高度
        
        for i in range(10):
            bds.append(building(random.randint(10, len - 10), random.randint(10, width - 10), random.randint(1, 10),
                                random.randint(1, 10), random.randint(9, 13)))
            map[bds[i].x - bds[i].l:bds[i].x + bds[i].l, bds[i].y - bds[i].w:bds[i].y + bds[i].w, 0:bds[i].h] = 1

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        for ob in bds:
            # 绘画出所有建筑
            x = ob.x
            y = ob.y
            z = 0
            dx = ob.l
            dy = ob.w
            dz = ob.h
            xx = np.linspace(x - dx, x + dx, 2)
            yy = np.linspace(y - dy, y + dy, 2)
            zz = np.linspace(z, z + dz, 2)

            xx2, yy2 = np.meshgrid(xx, yy)

            ax.plot_surface(xx2, yy2, np.full_like(xx2, z))
            ax.plot_surface(xx2, yy2, np.full_like(xx2, z + dz))

            yy2, zz2 = np.meshgrid(yy, zz)
            ax.plot_surface(np.full_like(yy2, x - dx), yy2, zz2)
            ax.plot_surface(np.full_like(yy2, x + dx), yy2, zz2)

            xx2, zz2 = np.meshgrid(xx, zz)
            ax.plot_surface(xx2, np.full_like(yy2, y - dy), zz2)
            ax.plot_surface(xx2, np.full_like(yy2, y + dy), zz2)
        plt.savefig('1.jpg')

        # 加载图片
        pixmap = QPixmap("1.jpg")

        self.label.setPixmap(pixmap)



        self.inputs2 = []

        dialog = InputDialog_3()


        my_list = []
        for i in bds:
            b_list = [i.x, i.y, i.l, i.w, i.h]
            my_list.append(b_list)
        for row in range(10):
            for column in range(5):
                item = QTableWidgetItem(f"{my_list[row][column]}")
                dialog.table.setItem(row, column, item)
        if dialog.exec_() == dialog.Accepted:
            print('输入框1:', dialog.get_inputs()[0])
            print('输入框2:', dialog.get_inputs()[1])
            print('输入框3:', dialog.get_inputs()[2])
            print('输入框4:', dialog.get_inputs()[3])
            print('输入框5:', dialog.get_inputs()[4])

        if dialog.get_inputs()[0]!='':
            bds.append(building(int(dialog.get_inputs()[0]), int(dialog.get_inputs()[1]), int(dialog.get_inputs()[2]), int(dialog.get_inputs()[3]), int(dialog.get_inputs()[4])))
            my_list = []
            for i in bds:
                b_list = [i.x, i.y, i.l, i.w, i.h]
                my_list.append(b_list)
            for row in range(10):
                for column in range(5):
                    item = QTableWidgetItem(f"{my_list[row][column]}")
                    dialog.table.setItem(row, column, item)
            self.is_use = 0
        my_2d_list = []
        for i in bds:
            b_list = [i.x, i.y, i.l, i.w, i.h]
            my_2d_list.append(b_list)
        # 将二维列表转换为DataFrame
        df = pd.DataFrame(my_2d_list, columns=['建筑中心X坐标', '建筑中心Y坐标', '建筑长半值', '建筑宽半值',
                                                   '建筑高度'])  # 您可以根据需要为列指定名称

        # 写入Excel文件
        excel_filename = 'output.xlsx'
        df.to_excel(excel_filename, index=False)


        print(bds)
        for ob in bds:
            # 绘画出所有建筑
            x = ob.x
            y = ob.y
            z = 0
            dx = ob.l
            dy = ob.w
            dz = ob.h
            xx = np.linspace(x - dx, x + dx, 2)
            yy = np.linspace(y - dy, y + dy, 2)
            zz = np.linspace(z, z + dz, 2)

            xx2, yy2 = np.meshgrid(xx, yy)

            ax.plot_surface(xx2, yy2, np.full_like(xx2, z))
            ax.plot_surface(xx2, yy2, np.full_like(xx2, z + dz))

            yy2, zz2 = np.meshgrid(yy, zz)
            ax.plot_surface(np.full_like(yy2, x - dx), yy2, zz2)
            ax.plot_surface(np.full_like(yy2, x + dx), yy2, zz2)

            xx2, zz2 = np.meshgrid(xx, zz)
            ax.plot_surface(xx2, np.full_like(yy2, y - dy), zz2)
            ax.plot_surface(xx2, np.full_like(yy2, y + dy), zz2)
        plt.savefig('2.jpg')

        # 加载图片
        pixmap = QPixmap("2.jpg")
        # 显示图片
        self.label.setPixmap(pixmap)
        # 自适应大小
        if dialog.get_inputs()[0] != '':
            dialog = InputDialog_3()
            my_list = []
            for i in bds:
                b_list = [i.x, i.y, i.l, i.w, i.h]
                my_list.append(b_list)
            for row in range(10):
                for column in range(5):
                    item = QTableWidgetItem(f"{my_list[row][column]}")
                    dialog.table.setItem(row, column, item)
            if dialog.exec_() == dialog.Accepted:
                print('输入框1:', dialog.get_inputs()[0])
                print('输入框2:', dialog.get_inputs()[1])
                print('输入框3:', dialog.get_inputs()[2])
                print('输入框4:', dialog.get_inputs()[3])
                print('输入框5:', dialog.get_inputs()[4])
            if dialog.get_inputs()[0]!='':
                bds.append(building(int(dialog.get_inputs()[0]), int(dialog.get_inputs()[1]), int(dialog.get_inputs()[2]),
                                    int(dialog.get_inputs()[3]), int(dialog.get_inputs()[4])))
                my_list = []
                for i in bds:
                    b_list = [i.x, i.y, i.l, i.w, i.h]
                    my_list.append(b_list)
                for row in range(10):
                    for column in range(5):
                        item = QTableWidgetItem(f"{my_list[row][column]}")
                        dialog.table.setItem(row, column, item)
                self.is_use = 0

            my_2d_list = []
            for i in bds:
                b_list = [i.x, i.y, i.l, i.w, i.h]
                my_2d_list.append(b_list)
            # 将二维列表转换为DataFrame
            df = pd.DataFrame(my_2d_list, columns=['建筑中心X坐标', '建筑中心Y坐标', '建筑长半值', '建筑宽半值',
                                                   '建筑高度'])  # 您可以根据需要为列指定名称

            # 写入Excel文件
            excel_filename = 'output.xlsx'
            df.to_excel(excel_filename, index=False)

        for ob in bds:
            # 绘画出所有建筑
            x = ob.x
            y = ob.y
            z = 0
            dx = ob.l
            dy = ob.w
            dz = ob.h
            xx = np.linspace(x - dx, x + dx, 2)
            yy = np.linspace(y - dy, y + dy, 2)
            zz = np.linspace(z, z + dz, 2)

            xx2, yy2 = np.meshgrid(xx, yy)

            ax.plot_surface(xx2, yy2, np.full_like(xx2, z))
            ax.plot_surface(xx2, yy2, np.full_like(xx2, z + dz))

            yy2, zz2 = np.meshgrid(yy, zz)
            ax.plot_surface(np.full_like(yy2, x - dx), yy2, zz2)
            ax.plot_surface(np.full_like(yy2, x + dx), yy2, zz2)

            xx2, zz2 = np.meshgrid(xx, zz)
            ax.plot_surface(xx2, np.full_like(yy2, y - dy), zz2)
            ax.plot_surface(xx2, np.full_like(yy2, y + dy), zz2)
        plt.savefig('2.jpg')
        # 加载图片
        pixmap = QPixmap("2.jpg")
        # 显示图片
        self.label.setPixmap(pixmap)
        # 自适应大小
        if os.path.isfile('测试.jpg'):
            df = pd.read_excel('output.xlsx')
            original_list = df.values.tolist()
            bds = []
            for i in original_list:
                bds.append(building(i[0], i[1], i[2], i[3], i[4]))
            my_list = []
            for i in bds:
                b_list = [i.x, i.y, i.l, i.w, i.h]
                my_list.append(b_list)
            for row in range(10):
                for column in range(5):
                    item = QTableWidgetItem(f"{my_list[row][column]}")
                    dialog.table.setItem(row, column, item)


        if dialog.get_inputs()[0] != '' and self.is_use ==1:
            pixmap = QPixmap("测试.jpg")
            # 显示图片
            self.label.setPixmap(pixmap)


        # if self.is_use==1:

        # self.is_use = 1
        # 加载图片
        # pixmap = QPixmap("测试.jpg")
        #
        # self.label.setPixmap(pixmap)

    def function3(self):
        LEARNING_RATE = 0.00033  # 学习率
        num_episodes = 80000  # 训练周期长度
        space_dim = 42  # n_spaces   状态空间维度
        action_dim = 27  # n_actions   动作空间维度
        threshold = 200
        env = Env(space_dim, action_dim, LEARNING_RATE)
        check_point_Qlocal = torch.load('Qlocal.pth')
        check_point_Qtarget = torch.load('Qtarget.pth')
        env.q_target.load_state_dict(check_point_Qtarget['model'])
        env.q_local.load_state_dict(check_point_Qlocal['model'])
        env.optim.load_state_dict(check_point_Qlocal['optimizer'])
        epoch = check_point_Qlocal['epoch']
        # 真实场景运行
        env.level = 7  # 环境难度等级
        state = env.reset_test()  # 环境重置1
        total_reward = 0
        env.render(1)
        n_done = 0
        count = 0

        n_test = 1  # 测试次数
        n_creash = 0  # 坠毁数目
        for i in range(n_test):
            while (1):
                if env.uavs[0].done:
                    # 无人机已结束任务，跳过
                    break
                action = env.get_action(FloatTensor(np.array([state[0]])), 0.01)  # 根据Q值选取动作

                next_state, reward, uav_done, info = env.step(action.item(), 0)  # 根据选取的动作改变状态，获取收益

                total_reward += reward  # 求总收益
                # 交互显示
                env.render()
                plt.savefig("function3.jpg")
                if uav_done:
                    break
                if info == 1:
                    success_count = success_count + 1

                state[0] = next_state  # 状态变更
            env.ax.scatter(env.target[0].x, env.target[0].y, env.target[0].z, c='red')

            # 加载图片
            pixmap = QPixmap("function3.jpg")
            # 调整图片大小以适应标签大小
            # pixmap = pixmap.scaledToWidth(300)
            # 显示图片
            self.label.setPixmap(pixmap)
            # 自适应大小
            self.label.setScaledContents(True)


    def function4(self):
        # 创建并显示输入对话框
        dialog = InputDialog_1(self)
        dialog.exec_()  # 显示模态对话框，等待用户关闭



class InputDialog_1(QDialog):
     def __init__(self, parent=None):
        super(InputDialog_1, self).__init__(parent)
        self.setWindowTitle('任务点设置')
        layout = QVBoxLayout()

            # 添加标签和输入框

        label = QLabel('最大转弯角（°）')
        line_edit = QLineEdit()
        layout.addWidget(label)
        layout.addWidget(line_edit)

        label = QLabel('最大爬升角（°）')
        line_edit = QLineEdit()
        layout.addWidget(label)
        layout.addWidget(line_edit)

        label = QLabel('最小飞行距离（m）')
        line_edit = QLineEdit()
        layout.addWidget(label)
        layout.addWidget(line_edit)

        label = QLabel('最小飞行高度（m）')
        line_edit = QLineEdit()
        layout.addWidget(label)
        layout.addWidget(line_edit)

        label = QLabel('最大飞行高度（m）')
        line_edit = QLineEdit()
        layout.addWidget(label)
        layout.addWidget(line_edit)

        label = QLabel('威胁系数（1）')
        line_edit = QLineEdit()
        layout.addWidget(label)
        layout.addWidget(line_edit)

        label = QLabel('飞行时间限制（s）')
        line_edit = QLineEdit()
        layout.addWidget(label)
        layout.addWidget(line_edit)

        label = QLabel('飞行时间限制（s）')
        line_edit = QLineEdit()
        layout.addWidget(label)
        layout.addWidget(line_edit)

        label = QLabel('飞行时间限制（s）')
        line_edit = QLineEdit()
        layout.addWidget(label)
        layout.addWidget(line_edit)

        exit_button = QPushButton('OK')
        layout.addWidget(exit_button)
        exit_button.clicked.connect(self.reject)
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.setLayout(layout)



class InputDialog_2(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(662, 533)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(270, 460, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 80, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 140, 111, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(80, 200, 111, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(80, 260, 111, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(80, 320, 111, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(80, 380, 111, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(240, 80, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 140, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(240, 200, 113, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(240, 260, 113, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(240, 320, 113, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(240, 380, 113, 21))
        self.lineEdit_6.setObjectName("lineEdit_6")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.setWindowFlags(Qt.Dialog | Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint)



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "任务点设置"))
        self.label.setText(_translate("Dialog", "目标点的坐标X："))
        self.label_2.setText(_translate("Dialog", "目标点的坐标Y："))
        self.label_3.setText(_translate("Dialog", "目标点的坐标Z："))
        self.label_4.setText(_translate("Dialog", "出发点的坐标X："))
        self.label_5.setText(_translate("Dialog", "出发点的坐标Y："))
        self.label_6.setText(_translate("Dialog", "出发点的坐标Z："))




    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)  # 去掉窗口上的问号
    def get_inputs(self):
        # 获取输入框的内容
        return self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text(), self.lineEdit_5.text(), self.lineEdit_6.text()





class InputDialog_3(QDialog):
    def setupUi(self,
                Dialog):
        Dialog.setObjectName("Dialog")
        self.setWindowTitle("环境配置")
        Dialog.resize(662, 533)
        self.table = QTableWidget(self)

        # 设置表格的行数和列数
        self.table.setRowCount(15)  # 例如，10行
        self.table.setColumnCount(5)  # 例如，5列
        self.table.setHorizontalHeaderLabels(['建筑中心坐标X', '建筑中心坐标Y', '建筑长半值L', '建筑高度H', '建筑宽W'])  # 设置列标题
        self.table.setGeometry(QtCore.QRect(40, 10, 600, 130))
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(280, 460, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(210, 340, 113, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(41, 280, 101, 20))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(31, 150, 111, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(31, 220, 111, 20))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(61, 400, 81, 20))
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(210, 280, 113, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(61, 340, 72, 15))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(210, 150, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 220, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(210, 400, 113, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(532, 500, 90, 26))

        self.pushButton_2.setObjectName("pushButton_2")


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.setWindowFlags(Qt.Dialog | Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint)
        self.pushButton_2.clicked.connect(self.function5)

    def function5(self):


        class building():
            def __init__(slf, x, y, l, w, h):
                slf.x = x  # 建筑中心x坐标
                slf.y = y  # 建筑中心y坐标
                slf.l = l  # 建筑长半值
                slf.w = w  # 建筑宽半值
                slf.h = h  # 建筑高度
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(None, "选择文件", "",
                                                  "All Files (*);;Text Files (*.txt)", options=options)
        file_name_only = os.path.basename(fileName)

        df = pd.read_excel(file_name_only)

        original_list = df.values.tolist()
        bds = []
        for i in original_list:
            bds.append(building(i[0],i[1],i[2],i[3],i[4]))

        for row in range(10):
            for column in range(5):
                item = QTableWidgetItem(f"{original_list[row][column]}")
                self.table.setItem(row, column, item)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        for ob in bds:
            # 绘画出所有建筑
            x = ob.x
            y = ob.y
            z = 0
            dx = ob.l
            dy = ob.w
            dz = ob.h
            xx = np.linspace(x - dx, x + dx, 2)
            yy = np.linspace(y - dy, y + dy, 2)
            zz = np.linspace(z, z + dz, 2)

            xx2, yy2 = np.meshgrid(xx, yy)

            ax.plot_surface(xx2, yy2, np.full_like(xx2, z))
            ax.plot_surface(xx2, yy2, np.full_like(xx2, z + dz))

            yy2, zz2 =  np.meshgrid(yy, zz)
            ax.plot_surface(np.full_like(yy2, x - dx), yy2, zz2)
            ax.plot_surface(np.full_like(yy2, x + dx), yy2, zz2)

            xx2, zz2 = np.meshgrid(xx, zz)
            ax.plot_surface(xx2, np.full_like(yy2, y - dy), zz2)
            ax.plot_surface(xx2, np.full_like(yy2, y + dy), zz2)
        plt.savefig('测试.jpg')

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "环境配置"))
        self.label.setText(_translate("Dialog", "建筑中心坐标X："))
        self.label_2.setText(_translate("Dialog", "建筑中心坐标Y："))
        self.label_3.setText(_translate("Dialog", "建筑长半值L："))
        self.label_5.setText(_translate("Dialog", "建筑高度H："))
        self.label_4.setText(_translate("Dialog", "建筑宽度W："))
        self.pushButton_2.setText(_translate("Dialog", "文件选择"))


    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)  # 去掉窗口上的问号



    def get_inputs(self):

        # 获取输入框的内容
        return self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text(), self.lineEdit_5.text()


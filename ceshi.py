from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton,QLineEdit


class GridLayoutExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建网格布局
        grid = QGridLayout()
        self.set
        # 创建输入框
        self.input1 = QLineEdit()
        self.input1.setPlaceholderText('请输入目标点的坐标X')
        grid.addWidget(self.input1, 0, 0)
        self.input2 = QLineEdit()
        self.input2.setPlaceholderText('请输入目标点的坐标Y')
        grid.addWidget(self.input2, 1, 0, 2, 1)
        self.input3 = QLineEdit()
        self.input3.setPlaceholderText('请输入目标点的坐标Z')
        grid.addWidget(self.input3, 0, 2, 1, 3)
        self.input4 = QLineEdit()
        self.input4.setPlaceholderText('请输入出发点的坐标X')
        self.input5 = QLineEdit()
        self.input5.setPlaceholderText('请输入出发点的坐标Y')
        self.input6 = QLineEdit()
        self.input6.setPlaceholderText('请输入出发点的坐标Z')




        # self.inputs.append(int(self.input1.text()))
        # self.inputs.append(int(self.input2.text()))
        # self.inputs.append(int(self.input3.text()))
        # self.inputs.append(int(self.input4.text()))
        # self.inputs.append(int(self.input5.text()))
        # self.inputs.append(int(self.input6.text()))
        # 创建确认按钮
        self.button_ok = QPushButton('确认')
        #self.button_ok.clicked.connect(self.accept)  # 接受输入
        grid.addWidget(self.button_ok)




        # # 添加按钮到网格布局中，指定位置和大小
        # btn1 = QPushButton('Button 1')
        # grid.addWidget(btn1, 0, 0)  # 在第0行第0列添加按钮1
        #
        # btn2 = QPushButton('Button 2')
        # grid.addWidget(btn2, 1, 0, 2, 1)  # 在第1行第0列添加按钮2，跨越2行，1列
        #
        # btn3 = QPushButton('Button 3')
        # grid.addWidget(btn3, 0, 1, 1, 2)  # 在第0行第1列添加按钮3，跨越1行，2列
        #
        # # 设置行和列的拉伸比例
        # grid.setRowStretch(2, 1)  # 设置第3行的拉伸比例为1
        # grid.setColumnStretch(2, 1)  # 设置第3列的拉伸比例为1
        #
        # # 设置间距
        grid.setHorizontalSpacing(10)  # 设置水平间距为10像素
        grid.setVerticalSpacing(10)  # 设置垂直间距为10像素
        #
        # # 设置对齐方式
        # #grid.setAlignment(btn3, Qt.AlignCenter)  # 将按钮3的对齐方式设置为居中

        # 将网格布局设置为窗口的布局
        self.setLayout(grid)


if __name__ == '__main__':
    app = QApplication([])
    ex = GridLayoutExample()
    ex.show()
    app.exec()

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import QThread, pyqtSignal
import time

class Worker(QThread):
    finished = pyqtSignal()

    def run(self):
        # 模拟耗时操作
        time.sleep(5)
        # 发送信号，表示功能执行完成
        self.finished.emit()

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('功能操作界面')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.button1 = QPushButton('功能1', self)
        self.button1.clicked.connect(self.function1)
        layout.addWidget(self.button1)

        self.button2 = QPushButton('功能2', self)
        self.button2.clicked.connect(self.function2)
        layout.addWidget(self.button2)

        self.button3 = QPushButton('功能3', self)
        self.button3.clicked.connect(self.function3)
        layout.addWidget(self.button3)

        self.setLayout(layout)

    def function1(self):
        self.button1.setEnabled(False)  # 禁用按钮，避免重复点击
        self.worker = Worker()
        self.worker.finished.connect(self.enable_button)
        self.worker.start()

    def enable_button(self):
        self.button1.setEnabled(True)  # 启用按钮

    def function2(self):
        # 实现功能2的代码
        print("执行功能2")

    def function3(self):
        # 实现功能3的代码
        print("执行功能3")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

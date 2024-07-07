from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from test import Ui_Form
from second import child1
from third import child2

class Mywindow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class child1(QMainWindow, child1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)
    def open(self):
        self.show()

class child2(QMainWindow, child2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def open(self):
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Mywindow()
    child1 = child1()
    #child2 = child2()
    window.show()
    window.pushButton.clicked.connect(child1.open)
    #child2.pushButton.clicked.connect(Ui_Form.function1)
    sys.exit(app.exec_())

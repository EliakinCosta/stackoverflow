import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MyApp(QApplication):

    def __init__(self, args):
        super().__init__(args)
        self.application_first_time_active = True# You need to know when is the first ApplicationActivate
        self.target_object = None

    def setTargetObject(self, obj):
        self.target_object = obj

    def event(self, event):
         if event.type() == QEvent.ApplicationActivated and self.application_first_time_active:
             self.target_object.initialize()
             self.application_first_time_active = False
         return super().event(event)


class CheckDemo(QWidget):

    def __init__(self, parent = None):
        super().__init__(parent)

        self.layout = QHBoxLayout()
        self.b1 = QCheckBox("Button1", self)
        self.b2 = QCheckBox("Button2", self)
        self.b3 = QCheckBox("Button3", self)

        self.layout.addWidget(self.b1)
        self.layout.addWidget(self.b2)
        self.layout.addWidget(self.b3)

        self.b1.setChecked(False)
        self.b2.setChecked(False)
        self.b3.setChecked(False)

        self.setLayout(self.layout)
        self.setWindowTitle("checkbox demo")

    def initialize(self):
        self.b2.setChecked(True)


def main():
    app = MyApp(sys.argv)
    ex = CheckDemo()
    app.setTargetObject(ex)
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

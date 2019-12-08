import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class CheckDemo(QWidget):

   def __init__(self, parent = None):
      super(CheckDemo, self).__init__(parent)

      self.layout = QHBoxLayout()
      self.b1 = QCheckBox("Button1")
      self.b2 = QCheckBox("Button2")
      self.b3 = QCheckBox("Button3")

      self.b1.setChecked(False)
      self.b2.setChecked(True)
      self.b3.setChecked(False)

      self.layout.addWidget(self.b1)
      self.layout.addWidget(self.b2)
      self.layout.addWidget(self.b3)
      self.setLayout(self.layout)
      self.setWindowTitle("checkbox demo")


def main():
   app = QApplication(sys.argv)
   ex = CheckDemo()
   ex.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()

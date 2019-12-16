from PyQt5.QtCore import QObject


class Window(QObject):

    def __init__(self, parent=None):
        super().__init__(parent)

    def textChangedd(self, text):
        print("blabla2")

from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QVBoxLayout
import sys
import importlib
import json


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.vBox = QVBoxLayout()
        self.entry = QLineEdit()
        self.vBox.addWidget(self.entry)
        self.plugins = []

        with open("package.json") as f:
            data = json.load(f)

        for plug in data["Plugin"]:
            plugin_module = importlib.import_module(
                "plugins.{}".format(plug["name"])
            )
            plugin_object = plugin_module.Window()
            self.entry.textChanged.connect(plugin_object.textChangedd)

            self.plugins.append(plugin_object)

        self.entry.textChanged.connect(self.textChanged)

        self.setLayout(self.vBox)
        self.show()

    def textChanged(self, text):
        if text == "close":
            app.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

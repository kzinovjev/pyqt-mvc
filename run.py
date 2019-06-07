from PyQt5 import QtWidgets, uic
import sys
from mvc import QMVCController


class TestController(QMVCController):

    @staticmethod
    def run():
        print('RUN!')


class WindowManager:

    def __init__(self):
        self.windows = {}

    def add(self, name, ui, widget):
        self.windows[name] = uic.loadUi(ui, widget)

    def __getitem__(self, name):
        return self.windows[name]


def bind_main_window(window, controller):
    controller.bind_lineEdit('text', window.textEdit)
    controller.listen('text', window.advancedButton.setText)
    window.runButton.clicked.connect(controller.run)


def run():
    app = QtWidgets.QApplication([])
    window_manager = WindowManager()
    controller = TestController()
    window_manager.add('main', 'main.ui', QtWidgets.QWidget())
    bind_main_window(window_manager['main'], controller)
    window_manager['main'].show()
    sys.exit(app.exec())


if __name__ == "__main__":
    run()

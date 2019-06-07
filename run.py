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


def bind_windows(window_manager, controller):
    main_window = window_manager['main']
    second_window = window_manager['second']

    controller.bind_lineEdit('text', main_window.textEdit)
    controller.listen('text', main_window.advancedButton.setText)
    main_window.runButton.clicked.connect(controller.run)
    main_window.advancedButton.clicked.connect(second_window.show)

    controller.bind_lineEdit('text', second_window.textEdit)
    controller.bind_slider('size', second_window.slider)
    controller.listen('size',
                      lambda size: second_window.sliderLabel.setText(str(size)))


def run():
    app = QtWidgets.QApplication([])
    window_manager = WindowManager()
    controller = TestController()

    window_manager.add('main', 'main.ui', QtWidgets.QWidget())
    window_manager.add('second', 'second.ui', QtWidgets.QWidget())
    bind_windows(window_manager, controller)

    window_manager['main'].show()
    sys.exit(app.exec())


if __name__ == "__main__":
    run()

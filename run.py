import sys
from controller import Controller
from windows import WindowManager, ManagedWindow
from PyQt5 import QtWidgets


class TestController(Controller):

    @staticmethod
    def run():
        print('RUN!')


class MainWindow(ManagedWindow):

    def __init__(self, window_manager):
        super().__init__('main', 'main.ui', window_manager)

    def bind(self, controller):
        self.bind_lineEdit(controller, 'text', self.textEdit)
        controller.listen('text', self.advancedButton.setText)
        self.runButton.clicked.connect(controller.run)
        self.advancedButton.clicked.connect(self.window_manager['second'].show)

    def closeEvent(self, event):
        self.window_manager.close_all()


class SecondWindow(ManagedWindow):

    def __init__(self, window_manager):
        super().__init__('second', 'second.ui', window_manager)

    def bind(self, controller):
        self.bind_lineEdit(controller, 'text', self.textEdit)
        self.bind_slider(controller, 'size', self.slider)
        controller.listen('size',
                          lambda size: self.sliderLabel.setText(str(size)))


def run():
    app = QtWidgets.QApplication([])
    window_manager = WindowManager()
    controller = TestController()

    MainWindow(window_manager)
    SecondWindow(window_manager)
    window_manager.bind_all(controller)

    window_manager['main'].show()
    sys.exit(app.exec())


if __name__ == "__main__":
    run()

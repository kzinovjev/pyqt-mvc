import sys
from mvc import QMVCController
from windows import *


class TestController(QMVCController):

    @staticmethod
    def run():
        print('RUN!')


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

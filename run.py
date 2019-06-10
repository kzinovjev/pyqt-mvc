import sys
from controller import Controller
from windows import WindowManager
from PyQt5 import QtWidgets

# Note that the code for each tab is stored in a separate module
from first import FirstTab
from second import SecondTab


class TestController(Controller):
    # Any 'business logic' that does not depend on PyQt (like writing out
    # inputs, running prep.py etc.) goes into controller.

    @staticmethod
    def run():
        print('RUN!')


class MainWindow(QtWidgets.QTabWidget):

    def __init__(self, window_manager):
        # There is no 'main.ui' file, since the main window is only a container
        # for tabs. Also, since it has no other widgets inside, nothing can
        # depend on the data and there is no need to register it in the
        # window manager (window_manager.add(...)).
        super().__init__()
        self.window_manager = window_manager
        self.setWindowTitle('MVC example')
        self.setFixedSize(220, 100)

    def closeEvent(self, event):
        self.window_manager.close_all()


def run():
    app = QtWidgets.QApplication([])
    window_manager = WindowManager()
    controller = TestController()

    main_window = MainWindow(window_manager)

    # Here SecondTab class is used as the second window.
    SecondTab('second', window_manager)

    main_window.addTab(FirstTab('tab1', window_manager), 'First')

    # Here SecondTab class is used to define a tab
    main_window.addTab(SecondTab('tab2', window_manager), 'Second')
    window_manager.bind_all(controller)

    main_window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    run()

import sys
from controller import Controller
from windows import WindowManager, ManagedWindow
from PyQt5 import QtWidgets


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


class FirstTab(ManagedWindow):

    def __init__(self, window_manager):
        super().__init__('tab1', 'first.ui', window_manager)

    def bind(self, controller):
        # Simple binding between text in textEdit and 'text' data field
        self.bind_lineEdit(controller, 'text', self.textEdit)

        # Example of a custom listener. Whenever 'text' field in the state
        # changes, the text on advancedButton will change too.
        controller.listen('text', self.advancedButton.setText)

        # Calling some code from the controller on click
        self.runButton.clicked.connect(controller.run)

        # Using window manager to show another window
        self.advancedButton.clicked.connect(self.window_manager['second'].show)

    def closeEvent(self, event):
        self.window_manager.close_all()


class SecondWindow(ManagedWindow):

    def __init__(self, window_manager, name='second'):
        # Here the constructor has an extra 'name' argument to allow registering
        # it two times in the window manager with different names: once as the
        # second tab in the main window and once as a separate window.
        super().__init__(name, 'second.ui', window_manager)

    def bind(self, controller):
        self.bind_lineEdit(controller, 'text', self.textEdit)
        self.bind_slider(controller, 'size', self.slider)
        controller.listen('size',
                          lambda size: self.sliderLabel.setText(str(size)))


def run():
    app = QtWidgets.QApplication([])
    window_manager = WindowManager()
    controller = TestController()

    main_window = MainWindow(window_manager)

    # Here SecondWindow class is used as another window. The name is not
    # provided, because the constructor has a default value defined ('second').
    SecondWindow(window_manager)

    main_window.addTab(FirstTab(window_manager), 'First')

    # Here SecondWindow class is used to define a tab
    main_window.addTab(SecondWindow(window_manager, 'tab2'), 'Second')
    window_manager.bind_all(controller)

    main_window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    run()

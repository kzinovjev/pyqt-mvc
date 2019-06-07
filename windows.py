from PyQt5 import QtWidgets, uic


class WindowManager:

    def __init__(self):
        self.windows = {}

    def bind_all(self, controller):
        for window in self.windows.values():
            window.bind(controller)

    def close_all(self):
        for window in self.windows.values():
            window.close()

    def add(self, name, ui, widget):
        print(name, ui)
        self.windows[name] = uic.loadUi(ui, widget)

    def __getitem__(self, name):
        return self.windows[name]


class ManagedWindow(QtWidgets.QWidget):

    def __init__(self, name, ui, window_manager):
        super().__init__()
        self.window_manager = window_manager
        window_manager.add(name, ui, self)

    def bind(self, controller):
        pass


class MainWindow(ManagedWindow):

    def __init__(self, window_manager):
        super().__init__('main', 'main.ui', window_manager)

    def bind(self, controller):
        controller.bind_lineEdit('text', self.textEdit)
        controller.listen('text', self.advancedButton.setText)
        self.runButton.clicked.connect(controller.run)
        self.advancedButton.clicked.connect(self.window_manager['second'].show)

    def closeEvent(self, event):
        self.window_manager.close_all()


class SecondWindow(ManagedWindow):

    def __init__(self, window_manager):
        super().__init__('second', 'second.ui', window_manager)
    
    def bind(self, controller):
        controller.bind_lineEdit('text', self.textEdit)
        controller.bind_slider('size', self.slider)
        controller.listen('size',
                          lambda size: self.sliderLabel.setText(str(size)))

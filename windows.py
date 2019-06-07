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

from PyQt5 import QtWidgets, uic


class WindowManager:
    """
    Simplifies interaction between windows. Each window must register itself in
    the window manager with a unique name. Then, the window can always be
    accessed through window manager as window_manager[name].
    """

    def __init__(self):
        self.windows = {}

    def bind_all(self, controller):
        """
        Instead of manually calling 'bind' method of each window, this method
        binds all the registered windows to the same controller.
        """
        for window in self.windows.values():
            window.bind(controller)

    def close_all(self):
        """
        The main window must call this method when closed, to ensure that all
        the other windows are closed too.
        """
        for window in self.windows.values():
            window.close()

    def add(self, name, widget):
        self.windows[name] = widget

    def __getitem__(self, name):
        """
        Allows to use window_manager[name] syntax
        """
        return self.windows[name]


class ManagedWindow(QtWidgets.QWidget):
    """
    Simplifies window management. Instead of manually registering every window
    in the window manager and then writing all the bidings, the managed window
    registers itself during the construction (window_manager.add) and also keeps
    all the code describing it's bindings (updaters and listeners).
    It also loads the layout (.ui file) and has some helper methods to
    simplify binding of common input widgets (lineEdit, checkBox, slider).
    """

    def __init__(self, name, ui, window_manager):
        super().__init__()
        self.window_manager = window_manager
        window_manager.add(name, uic.loadUi(ui, self))

    def bind(self, controller):
        """
        All the binding code for the window goes here. That way the code for
        each window is kept in the corresponding class.
        """
        raise NotImplementedError

    @staticmethod
    def bind_lineEdit(controller, key, lineEdit):
        """
        Binds lineEdit text to the data point defined by 'key': whenever
        the user types something in the provided lineEdit, the controller will
        be informed and will call all the listeners for the given key. And
        vice versa: whenever by any reason the data changes, the controller
        will call the setText method of lineEdit with the changed data.
        """
        # Here note that controller.updater(key) returns a function, which,
        # whenever the text in lineEdit is changed, will change the data.
        lineEdit.textChanged.connect(controller.updater(key))
        # the method lineEdit.setText is used as a listener, so the text will
        # be changed whenever the data changes
        controller.listen(key, lineEdit.setText)

    @staticmethod
    def bind_checkBox(controller, key, checkBox):
        checkBox.toggled.connect(controller.updater(key))
        controller.listen(key, checkBox.setChecked)

    @staticmethod
    def bind_slider(controller, key, slider):
        slider.valueChanged.connect(controller.updater(key))
        controller.listen(key, slider.setValue)

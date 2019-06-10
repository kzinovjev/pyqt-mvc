from windows import ManagedWindow


class SecondTab(ManagedWindow):

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

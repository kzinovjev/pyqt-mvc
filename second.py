from windows import ManagedWindow


class SecondTab(ManagedWindow):

    def __init__(self, name, window_manager):
        super().__init__(name, 'second.ui', window_manager)

    def bind(self, controller):
        self.bind_lineEdit(controller, 'text', self.textEdit)
        self.bind_slider(controller, 'size', self.slider)
        controller.listen('size',
                          lambda size: self.sliderLabel.setText(str(size)))

class MVCController:

    def __init__(self):
        self.state = {}
        self.listeners = {}

    def update(self, key, value):
        self.state[key] = value
        print(self.state)
        for listener in self._get_listeners(key):
            listener(value)

    def updater(self, key):
        return lambda value: self.update(key, value)

    def listen(self, key, listener):
        self.listeners[key] = self._get_listeners(key) + [listener]

    def _get_listeners(self, key):
        return self.listeners.get(key, [])


class QMVCController(MVCController):

    def bind_lineEdit(self, key, lineEdit):
        lineEdit.textChanged.connect(self.updater(key))
        self.listen(key, lineEdit.setText)

    def bind_checkBox(self, key, checkBox):
        checkBox.toggled.connect(self.updater(key))
        self.listen(key, checkBox.setChecked)

    def bind_slider(self, key, slider):
        slider.sliderMoved.connect(self.updater(key))
        self.listen(key, slider.setValue)

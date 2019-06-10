from windows import ManagedWindow


class FirstTab(ManagedWindow):

    def __init__(self, name, window_manager):
        super().__init__(name, 'first.ui', window_manager)

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

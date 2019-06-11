class Controller:
    """
    Is responsible for data management. All the data is stored in the state
    field of the controller and must only be changed by calling the 'update'
    method of the controller. That way the controller always knows when the
    state is changed and can inform all the 'listeners' about the change. A
    listener is a callback (a function) that a window can provide to the
    controller when it wants to know that a particular piece of data is changed.
    Then, whenever this data changes, the controller will call the listener with
    the new value of the data as an argument.
    """

    def __init__(self):
        self.state = {}
        self.listeners = {}

    def update(self, key, value):
        """
        Updates the data and calls all the corresponding listeners
        """
        if self.state.get(key, None) == value:
            return
        self.state[key] = value
        print(self.state)
        for listener in self._get_listeners(key):
            listener(value)

    def updater(self, key):
        """
        Returns a callback which, when called, changes the data.
        Useful for bindings in Qt widgets.
        """
        return lambda value: self.update(key, value)

    def listen(self, key, listener):
        """
        Registers a listener for the given key
        """
        self.listeners[key] = self._get_listeners(key) + [listener]

    def _get_listeners(self, key):
        return self.listeners.get(key, [])

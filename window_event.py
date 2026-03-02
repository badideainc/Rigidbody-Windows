class WindowEvent:
    def __init__(self, window):
        self.window = window

class WindowCollisionEvent(WindowEvent):
    def __init__(self, window, other_window):
        super().__init__(window)
        self.other_window = other_window
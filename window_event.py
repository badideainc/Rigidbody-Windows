from window_math import Vector2

class WindowEvent:
    def __init__(self, window):
        self.window = window

class WindowCollisionEvent(WindowEvent):
    def __init__(self, window, other_window):
        super().__init__(window)
        self.other_window = other_window

class WindowClickEvent(WindowEvent):
    def __init__(self, window, x, y):
        super().__init__(window)
        self.position = Vector2(x, y)


import inspect

class ScreenListener:
    def __init__(self):
        self.windows = []

    def add_window(self, window):
        self.windows.append(window)
    
    def listen(self):
        while True:
            for window in self.windows:
                window.update()
                if (self.has_event(window, "onClick")):
                    print("Window has onClick event")

    def has_event(self, window, eventName):
        for component in window.components:
            if hasattr(component, eventName):
                return True
        return False
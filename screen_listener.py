class ScreenListener:
    def __init__(self):
        self.windows = []

    def add_window(self, window):
        self.windows.append(window)
    
    def listen(self):
        pass
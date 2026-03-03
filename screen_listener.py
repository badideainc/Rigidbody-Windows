class ScreenListener:
    def __init__(self):
        self.windows = []

    def add_window(self, window):
        self.windows.append(window)
    
    def listen(self):
        while True:
            for window in self.windows:
                window.update()
                if (window.hasOnClick):
                    print("Window has onClick event")
                if (window.hasOnEnterCollision):
                    print("Window has onEnterCollision event")
                if (window.hasOnExitCollision):
                    print("Window has onExitCollision event")
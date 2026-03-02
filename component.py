
class Component:
    def __init__(self, id, window, startTime):
        self.id = id
        self.window = window
        self.start_time = startTime
    
    #Listen for events
    def listen(self):
        pass

    def onClick(self, event):
        pass

    def onEnterCollision(self, event):
        pass

    def onExitCollision(self, event):
        pass

    def update(self):
        pass
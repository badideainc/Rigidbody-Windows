from window_event import *

class Component:
    def __init__(self, id, window, startTime):
        self.id = id
        self.window = window
        self.start_time = startTime
    
    #Listen for events
    def listen(self):
        pass

    #On mouse click on window
    def onClick(self, event):
        pass

    #On window collision with another window
    def onEnterCollision(self, event):
        pass

    #On window exit collision with another window
    def onExitCollision(self, event):
        pass

    def update(self):
        pass
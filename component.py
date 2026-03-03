from window_event import *

class Component:
    def __init__(self, id, window, screen, startTime):
        self.id = id
        self.window = window
        self.screen = screen
        self.start_time = startTime

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
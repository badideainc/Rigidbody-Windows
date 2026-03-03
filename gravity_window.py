import time
from component import Component

class GravityWindowComponent(Component):
    def __init__(self, id, window, screen, startTime):
        super().__init__(id, window, screen, startTime)

        self._gravity_constant = 9.81

        self._start_time = time.perf_counter()

    def _gravity(self):
        if (self.window.y + self.window.height < self.screen.height):
                dy = int(self._acceleration(time.perf_counter() - self._start_time))
                self.window.move(self.window.x, self.window.y + dy)
            
    def onClick(self, event):
        self._start_time = time.perf_counter()

    def _acceleration(self, time):
        return 0.5 * self._gravity_constant * time**2
    
    def update(self):
        self._gravity()
